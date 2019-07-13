import logging
from PyQt5 import QtCore, QtWidgets

from anchor.core.core_settings import app_settings
from anchor.core.jira_interactor import JiraInteractor
from anchor.model.app_data import Ticket


class TicketStatePresenter:
    selected_ticket: Ticket

    def __init__(self, parent_view):
        self.parent_view = parent_view
        self.selected_ticket = None
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.buttonClicked[QtWidgets.QAbstractButton].connect(self.handle_state_transition)
        app_settings.app_data.signals.ticket_changed.connect(self.refresh)
        self.jira_interactor = JiraInteractor()

    def refresh(self, ticket):
        self.selected_ticket = ticket

        for existing_button in self.button_group.buttons():
            existing_button.hide()
            self.parent_view.verticalLayout_2.removeWidget(existing_button)

        _translate = QtCore.QCoreApplication.translate
        logging.info("Updating Ticket State presenter")
        for transition in self.selected_ticket.ticket_transitions:
            transition_id = transition.get("id")
            transition_name = transition.get("name")
            btn = QtWidgets.QPushButton(self.parent_view.centralwidget)
            btn.setObjectName(transition_id)
            self.parent_view.verticalLayout_2.addWidget(btn)
            btn.setText(_translate("MainWindow", transition_name))
            self.button_group.addButton(btn)

    def handle_state_transition(self, button):
        logging.info(f"Handling state transition {button.objectName()} to {button.text()}")
        transition = next(
            (tr for tr in self.selected_ticket.ticket_transitions if tr.get("id") == button.objectName()),
            None
        )
        args = {
            'ticket': self.selected_ticket,
            'transition': transition,
            'on_success': self.on_success,
            'on_failure': self.on_failure
        }
        self.parent_view.show_progress_dialog(
            f"Updating status of {self.selected_ticket.ticket_number} to {button.text()}")
        self.jira_interactor.update_transition(**args)

    def on_success(self, result):
        ticket = result.get('ticket')
        self.parent_view.hide_progress_dialog()
        app_settings.app_data.transition_state(ticket.ticket_number, ticket.ticket_url)

    def on_failure(self, result):
        logging.error("Unable to change state")
        logging.error(result)
