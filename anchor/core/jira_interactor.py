from anchor.core.worker_pool import pool
from anchor.external.jira_connector import ApiType
from anchor.external.jira_connector import JiraConnector


class JiraInteractor:

    def check_connectivity(self, **kwargs):
        self._start_worker(ApiType.CONNECT, **kwargs)

    def fetch_ticket_details(self, **kwargs):
        self._start_worker(ApiType.TICKET_DETAILS, **kwargs)

    def fetch_all_tickets(self, **kwargs):
        self._start_worker(ApiType.FETCH_ALL_TICKETS, **kwargs)

    def update_transition(self, **kwargs):
        self._start_worker(ApiType.UPDATE_TICKET_TRANSITION, **kwargs)

    def _start_worker(self, api_type, **kwargs):
        jira_worker = JiraConnector(api_type, **kwargs)
        jira_worker.signals.result.connect(kwargs['on_success'])
        jira_worker.signals.error.connect(kwargs['on_failure'])
        pool.schedule(jira_worker)
