import logging


class MockJiraApi:
    tickets = []

    def __init__(self):
        logging.debug("Setup Mock data here")
        for i in range(10):
            ticket = dict(
                id=i,
                key=f"TECH-{i}",
                self=f"http://local/TECH-{i}",
                fields=dict(
                    summary=f"Mock Ticket summary for Tech-{i}",
                    status=dict(
                        name="In Progress"
                    )
                ),
                renderedFields=dict(
                    description=f"<h1>Mock Ticket Summary for Tech-{i}</h1>",
                    updated="Last week"
                ),
                transitions=[dict(
                    id=f"TR-{i}",
                    name="Done"
                )]
            )
            self.tickets.append(ticket)

    def connect(self):
        logging.debug("Connecting to Mock JIRA Api")
        return {}

    def get_tickets(self):
        logging.debug("Getting all tickets using Mock JIRA Api")
        return {
            "issues": self.tickets
        }

    def get_ticket(self, resource):
        logging.debug("Get single ticket using Mock JIRA Api")
        logging.debug(resource)
        return next((t for t in self.tickets if t.get("self") == resource), None)

    def update_transition(self, ticket_id, transition_id):
        logging.debug("Update Transition using Mock JIRA Api")
        return {}
