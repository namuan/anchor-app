import os

from anchor.external import requester
from anchor.external.mock_jira_apis import MockJiraApi

is_offline = os.getenv("MOCKED", "false").lower() == "true"


class JiraApi:
    server: str
    user: str
    password: str

    @classmethod
    def auth(cls, *args):
        if is_offline:
            mock_jira_api = MockJiraApi()
            return mock_jira_api

        server, user, password = args
        jira_api = cls()
        jira_api.server = server
        jira_api.user = user
        jira_api.password = password
        return jira_api

    def connect(self):
        resource = f"{self.server}/rest/api/2/issue/createmeta"
        return requester.request_get(resource, self.user, self.password)

    def get_tickets(self):
        resource = f"{self.server}/rest/api/2/search"
        query = {
            "jql": "assignee=currentUser() AND resolution = Unresolved ORDER BY updated DESC",
            "expand": [
                "transitions",
                "renderedFields"
            ],
            "fields": [
                "id",
                "key",
                "description",
                "summary",
                "updated",
                "status"
            ]
        }

        return requester.request_post(resource, self.user, self.password, query)

    def get_ticket(self, resource):
        params = {
            "expand": "transitions,renderedFields",
            "fields": "id,key,description,summary,updated,status",
        }
        return requester.request_get(resource, self.user, self.password, params)

    def update_transition(self, ticket_id, transition_id):
        resource = f"{self.server}/rest/api/2/issue/{ticket_id}/transitions"
        request_body = {
            "transition": {
                "id": transition_id
            }
        }
        return requester.request_post(resource, self.user, self.password, request_body)
