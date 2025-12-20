import logging

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon

from anchor.core.core_settings import app_settings
from anchor.core.jira_interactor import JiraInteractor
from anchor.ui.widgets.ticket_widget import TicketWidget


class TicketsListPresenter:
    def __init__(self, tickets_list, parent_view):
        self.parent_view = parent_view
        self.tickets_list_widget = tickets_list
        self.tickets_list_widget.clicked.connect(self.on_double_clicked)
        self.jira_interactor = JiraInteractor()
        app_settings.app_data.signals.index_changed.connect(self.refresh)
        app_settings.app_data.signals.ticket_transition_changed.connect(self.refresh_ticket)
        self.story_icon = QIcon("images:notifier-48.png")

    def refresh(self):
        self.tickets_list_widget.clear()
        for number, status, url, title in app_settings.app_data.get_visible_tickets():
            ticket_widget = TicketWidget(self.parent_view)
            ticket_widget.set_data(number, status, title, url)
            ticket_widget_item = QtWidgets.QListWidgetItem(self.tickets_list_widget)
            ticket_widget_item.setSizeHint(ticket_widget.sizeHint())

            self.tickets_list_widget.addItem(ticket_widget_item)
            self.tickets_list_widget.setItemWidget(ticket_widget_item, ticket_widget)

    def on_double_clicked(self):
        item = self.tickets_list_widget.itemWidget(self.tickets_list_widget.selectedItems()[0])
        ticket_number, _, ticket_url = item.get_data()
        logging.info(f"Clicked {ticket_number} with url {ticket_url}")
        self.refresh_ticket(ticket_number, ticket_url)

    def refresh_ticket(self, ticket_number, ticket_url):
        self.parent_view.show_progress_dialog(f"Fetching details for {ticket_number}")
        args = {
            'ticket_number': ticket_number,
            'ticket_url': ticket_url,
            'on_success': self.on_success,
            'on_failure': self.on_failure
        }
        self.jira_interactor.fetch_ticket_details(**args)

    def on_success(self, result):
        self.parent_view.hide_progress_dialog()
        ticket = result.get('ticket')
        app_settings.app_data.upsert_ticket(ticket.ticket_number, ticket)

    def on_failure(self, result):
        logging.error("Unable to get ticket details")
        logging.error(result)
