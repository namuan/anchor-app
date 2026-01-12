import os

from jira import JIRA

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
        jira = JIRA(self.server, basic_auth=(self.user, self.password))
        try:
            myself = jira.myself()
            return myself
        except Exception as e:
            raise ConnectionError(e)

    def get_tickets(self):
        jira = JIRA(self.server, basic_auth=(self.user, self.password))

        jql = "project = FRN AND status IN (New, Ready, \"In Progress\") AND type IN (Story, Bug)"
        fields = "id,key,description,summary,updated,status"
        expand = "transitions,renderedFields"

        issues = jira.search_issues(jql_str=jql, fields=fields, expand=expand, json_result=True)
        return issues

    def get_ticket(self, resource):
        # Resource is expected to be the 'self' URL in the old implementation
        # But for JIRA lib, it's easier to use the key or ID.
        # However, the calling code passes 'ticket_url' as 'resource'.
        # We need to extract the key from the URL or just assume the caller might change.
        # Looking at usage in jira_connector.py:
        # jira_ticket_json = JiraApi.auth(*app_settings.load_jira_configuration()).get_ticket(ticket_url)
        # It passes ticket_url.
        # We need to parse the key from the url or find a way to fetch by self url.
        # Actually, jira.issue() takes a key or ID.
        # Let's try to extract the key from the resource URL if possible, or just fail if it's not a key.
        # BUT wait, the old implementation did a GET on the resource URL.
        # If we want to be safe, we should extract the ticket key.
        # A simple split could work if the URL structure is standard.
        # resource example: .../rest/api/2/issue/TECH-0

        ticket_id = resource.split('/')[-1]

        jira = JIRA(self.server, basic_auth=(self.user, self.password))

        fields = "id,key,description,summary,updated,status"
        expand = "transitions,renderedFields"

        issue = jira.issue(ticket_id, fields=fields, expand=expand)
        return issue.raw

    def update_transition(self, ticket_id, transition_id):
        jira = JIRA(self.server, basic_auth=(self.user, self.password))
        jira.transition_issue(ticket_id, transition=transition_id)
        return {}
