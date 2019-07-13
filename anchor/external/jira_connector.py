import logging

from enum import Enum
from operator import itemgetter

from PyQt5.QtCore import QRunnable, QObject, pyqtSignal, pyqtSlot

from anchor.external.jira_apis import JiraApi
from anchor.model.app_data import Ticket
from anchor.core.core_settings import app_settings


class ConfigCheckSignals(QObject):
    result = pyqtSignal(dict)
    error = pyqtSignal(dict)


ApiType = Enum('ApiType', 'CONNECT TICKET_DETAILS FETCH_ALL_TICKETS UPDATE_TICKET_TRANSITION')


class JiraConnector(QRunnable):

    def __init__(self, api_type, **kwargs):
        super(JiraConnector, self).__init__()
        self.signals = ConfigCheckSignals()
        self.api_type = api_type
        self.args = kwargs
        self.api_type_func = {
            ApiType.CONNECT: self.check_connection,
            ApiType.TICKET_DETAILS: self.ticket_details,
            ApiType.FETCH_ALL_TICKETS: self.fetch_all_tickets,
            ApiType.UPDATE_TICKET_TRANSITION: self.update_ticket_transition
        }

    def update_ticket_transition(self):
        ticket = self.args.get('ticket')
        ticket_id = ticket.ticket_id
        transition_id = self.args.get('transition').get('id')
        logging.info(f"Updating ticket {ticket_id} transition to {transition_id}")
        try:
            JiraApi.auth(*app_settings.load_jira_configuration()).update_transition(ticket_id, transition_id)
            result = {
                'ticket': ticket
            }
            self.signals.result.emit(result)
        except ConnectionError as e:
            error = {
                'message': e.__str__(),
                'exception': e
            }
            self.signals.error.emit(error)

    def fetch_all_tickets(self):
        logging.info("Fetching all tickets")
        try:
            all_jira_tickets = JiraApi.auth(*app_settings.load_jira_configuration()).get_tickets()
            tickets = [Ticket.from_issue_json(t) for t in all_jira_tickets.get('issues', [])]
            result = {
                'tickets': tickets
            }
            self.signals.result.emit(result)
        except ConnectionError as e:
            error = {
                'message': e.__str__(),
                'exception': e
            }
            self.signals.error.emit(error)

    def ticket_details(self):
        ticket_url = self.args['ticket_url']
        logging.info(f"Fetching ticket details - {ticket_url}")
        try:
            jira_ticket_json = JiraApi.auth(*app_settings.load_jira_configuration()).get_ticket(ticket_url)
            ticket = Ticket.from_issue_json(jira_ticket_json)
            t = {
                'ticket': ticket
            }
            self.signals.result.emit(t)
        except ConnectionError as e:
            error = {
                'message': e.__str__(),
                'exception': e
            }
            self.signals.error.emit(error)

    def check_connection(self):
        logging.info("Checking connection")
        try:
            JiraApi.auth(*itemgetter('server', 'username', 'password')(self.args)).connect()
            self.signals.result.emit(self.args)
        except ConnectionError as e:
            error = {
                'message': e.__str__(),
                'exception': e
            }
            self.signals.error.emit(error)

    @pyqtSlot()
    def run(self):
        logging.info("Running JIRA Connector ")
        self.api_type_func.get(self.api_type)()
