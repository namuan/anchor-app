import logging
from typing import Optional

from PyQt6.QtWidgets import QApplication

from anchor.core.core_settings import app_settings
from anchor.model.app_data import Ticket


class TicketContentPresenter:
    selected_ticket: Optional[Ticket]
    no_tickets_selected_title: str = "👈  Please select a ticket"

    def __init__(self, parent_view):
        self.parent_view = parent_view
        self.selected_ticket = None
        self.lbl_title = self.parent_view.lbl_ticket_title
        self.txt_ticket_notes = self.parent_view.txt_ticket_notes
        self.web_engine = self.parent_view.web_engine
        self.lbl_title.setText(self.no_tickets_selected_title)
        app_settings.app_data.signals.ticket_changed.connect(self.refresh)
        self.parent_view.btn_copy_ticket.clicked.connect(self.ticket_to_clipboard)
        QApplication.instance().focusChanged.connect(self.ticket_notes_changed)

    def ticket_notes_changed(self, old, new):
        if old is not self.txt_ticket_notes:
            return

        if not self.selected_ticket:
            return

        updated_notes = self.txt_ticket_notes.toPlainText()
        if self.selected_ticket.ticket_notes == updated_notes:
            return

        app_settings.app_data.add_ticket_notes(
            self.selected_ticket.ticket_number, updated_notes
        )

    def ticket_to_clipboard(self):
        if not self.selected_ticket:
            return
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Mode.Clipboard)
        clipboard.setText(
            self.selected_ticket.ticket_number, mode=clipboard.Mode.Clipboard
        )

    def refresh(self, ticket):
        self.selected_ticket = ticket

        logging.info("Refreshing data for ticket content")
        self.parent_view.btn_copy_ticket.setEnabled(self.selected_ticket is not None)

        jira_server, _, _, _ = app_settings.load_jira_configuration()
        ticket_browse_link = (
            f"{jira_server}/browse/{self.selected_ticket.ticket_number}"
        )
        ticket_title = f'<a href="{ticket_browse_link}">{self.selected_ticket.ticket_number}</a> - {self.selected_ticket.ticket_title}'
        if not self.selected_ticket:
            self.lbl_title.setText(self.no_tickets_selected_title)
        else:
            self.lbl_title.setText(ticket_title)
        self.txt_ticket_notes.setPlainText(self.selected_ticket.ticket_notes)
        description_html = (
            self.selected_ticket.ticket_description
            or "<p>Ticket description is unavailable at the moment.</p>"
        )
        logging.info(
            f"Ticket description for {self.selected_ticket.ticket_number}: {description_html}"
        )
        self.web_engine.setHtml(description_html)
