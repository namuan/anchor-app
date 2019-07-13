import logging

from PyQt5.QtCore import QObject, pyqtSignal
from tinydb import TinyDB, Query


class Ticket:
    def __init__(self, **kwargs):
        self.type = 'ticket'
        self.ticket_id = None
        self.ticket_number = None
        self.ticket_url = None
        self.ticket_title = None
        self.ticket_status = None
        self.ticket_description = None
        self.ticket_transitions = []
        self.ticket_comments = []
        self.last_updated = None
        self.workspace_dir = None
        self.ticket_notes = None
        self.__dict__.update(kwargs)

    def to_json(self):
        _json = {
            'type': self.type,
            'ticket_id': self.ticket_id,
            'ticket_number': self.ticket_number,
            'ticket_url': self.ticket_url,
            'ticket_title': self.ticket_title,
            'ticket_status': self.ticket_status,
            'ticket_description': self.ticket_description,
            'last_updated': self.last_updated,
            'workspace_dir': self.workspace_dir,
            'ticket_notes': self.ticket_notes,
            'ticket_comments': [c for c in self.ticket_comments],
            'ticket_transitions': [tt for tt in self.ticket_transitions]
        }
        return {k: v for k, v in _json.items() if v and v is not None}

    @classmethod
    def from_json(cls, json_obj):
        c = cls()
        c.ticket_id = json_obj.get('ticket_id', None)
        c.ticket_number = json_obj.get('ticket_number', None)
        c.ticket_url = json_obj.get('ticket_url', None)
        c.ticket_title = json_obj.get('ticket_title', None)
        c.ticket_status = json_obj.get('ticket_status', None)
        c.ticket_description = json_obj.get('ticket_description', None)
        c.last_updated = json_obj.get('last_updated', None)
        c.workspace_dir = json_obj.get('workspace_dir', None)
        c.ticket_notes = json_obj.get('ticket_notes', None)
        c.ticket_comments = [c for c in json_obj.get('ticket_comments', [])]
        c.ticket_transitions = [tt for tt in json_obj.get('ticket_transitions', [])]
        return c

    @classmethod
    def from_issue_json(cls, issue_json):
        c = cls()
        c.ticket_id = issue_json.get('id', None)
        c.ticket_number = issue_json.get('key', None)
        c.ticket_url = issue_json.get('self', None)
        c.ticket_title = issue_json.get('fields').get('summary')
        c.ticket_status = issue_json.get('fields').get('status').get('name')
        c.ticket_description = issue_json.get('renderedFields').get('description')
        c.ticket_transitions = issue_json.get('transitions', [])
        c.last_updated = issue_json.get('renderedFields').get('updated')
        return c


class AppDataSignals(QObject):
    ticket_changed = pyqtSignal(Ticket)
    app_changed = pyqtSignal(str)
    index_changed = pyqtSignal()
    ticket_transition_changed = pyqtSignal(str, str)
    branch_changed = pyqtSignal(str)


class AppData:
    db: TinyDB

    def __init__(self, db):
        self.db = db
        self.signals = AppDataSignals()

    def add_visible_tickets(self, tickets):
        logging.info(f"Setting visible tickets")
        VisibleTickets = Query()
        self.db.upsert({'type': 'index',
                        'keys': [(t.ticket_number, t.ticket_status, t.ticket_url, t.ticket_title) for t in tickets]},
                       VisibleTickets.type == 'index')
        self.signals.index_changed.emit()

    def get_visible_tickets(self):
        VisibleTickets = Query()
        document = self.db.get(VisibleTickets.type == 'index')
        if document:
            return document.get('keys')

        return []

    def add_app(self, app_path):
        logging.info(f"Adding App: App Path: {app_path}")
        App = Query()
        self.db.upsert({'type': 'app', 'path': app_path}, App.path == app_path)
        self.signals.app_changed.emit(app_path)

    def get_apps(self):
        App = Query()
        return self.db.search(App.type == 'app')

    def get_tickets(self):
        TicketQuery = Query()
        return [Ticket.from_json(t) for t in self.db.search(TicketQuery.type == 'ticket')]

    def get_ticket(self, ticket_number):
        logging.info(f"Get Ticket: {ticket_number}")
        TicketQuery = Query()
        db_ticket = self.db.get(TicketQuery.ticket_number == ticket_number)
        if not db_ticket:
            return None

        return Ticket.from_json(db_ticket)

    def upsert_ticket(self, ticket_number, ticket):
        logging.info(f"Upsert Ticket: Ticket: {ticket_number}")
        TicketQuery = Query()
        self.db.upsert(ticket.to_json(), TicketQuery.ticket_number == ticket_number)
        new_ticket = Ticket.from_json(self.db.get(TicketQuery.ticket_number == ticket_number))
        self.signals.ticket_changed.emit(new_ticket)
        return new_ticket

    def add_workspace(self, ticket_number, workspace_dir):
        logging.info(f"Adding workspace: Ticket: {ticket_number}, Workspace Dir: {workspace_dir}")
        TicketQuery = Query()
        ticket = Ticket.from_json(self.db.get(TicketQuery.ticket_number == ticket_number))
        ticket.workspace_dir = workspace_dir
        self.db.upsert(ticket.to_json(), TicketQuery.ticket_number == ticket_number)
        updated_ticket = self.get_ticket(ticket_number)
        self.signals.ticket_changed.emit(updated_ticket)
        return updated_ticket

    def add_ticket_notes(self, ticket_number, ticket_notes):
        logging.info(f"Adding notes to Ticket: {ticket_number}")
        TicketQuery = Query()
        ticket = Ticket.from_json(self.db.get(TicketQuery.ticket_number == ticket_number))
        ticket.ticket_notes = ticket_notes
        self.db.upsert(ticket.to_json(), TicketQuery.ticket_number == ticket_number)
        updated_ticket = self.get_ticket(ticket_number)
        self.signals.ticket_changed.emit(updated_ticket)
        return updated_ticket

    def transition_state(self, number, url):
        self.signals.ticket_transition_changed.emit(number, url)

    def update_branch(self, workspace_dir):
        self.signals.branch_changed.emit(workspace_dir)
