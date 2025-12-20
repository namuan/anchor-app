from unittest import TestCase

from anchor.model.app_data import create_or_open, Ticket


class TestAppData(TestCase):
    app_data = None

    @classmethod
    def setUpClass(cls):
        cls.app_data = create_or_open("test.json")
        cls.app_data.db.drop_tables()

    def test_add_app_to_ticket(self):
        # setup
        app_path = "/Applications/VScode"

        # test
        self.app_data.add_app(app_path)

        # assert
        self.assertTrue(app_path in [app.get('path') for app in self.app_data.get_apps()])

    def test_get_ticket_details(self):
        # setup
        ticket_number = "DEV-0001"
        ticket_url = "http://DEV-123123"
        self.app_data.upsert_ticket(ticket_number, Ticket(ticket_number=ticket_number, ticket_url=ticket_url))

        # test
        expected_ticket = self.app_data.get_ticket(ticket_number)

        # assert
        assert expected_ticket is not None
        assert expected_ticket.ticket_url == ticket_url

    def test_add_workspace(self):
        # setup
        ticket_number = "DEV-12345"
        self.app_data.upsert_ticket(ticket_number, Ticket(ticket_number=ticket_number))
        workspace_dir = "~/workspace"

        # test
        self.app_data.add_workspace(ticket_number, workspace_dir)

        # assert
        expected_ticket = self.app_data.get_ticket(ticket_number)
        assert expected_ticket.workspace_dir == workspace_dir

    def test_add_new_ticket(self):
        # setup
        ticket_number = "DEV-00012"
        ticket_url = "http://devsd"
        workspace_dir = "/Applications/Anchor"
        existing_ticket = self.app_data.get_ticket(ticket_number)
        self.assertFalse(existing_ticket)
        t = Ticket(ticket_number=ticket_number, ticket_url=ticket_url, workspace_dir=workspace_dir)

        # test
        new_ticket = self.app_data.upsert_ticket(ticket_number, t)

        # assert
        assert new_ticket.ticket_number == ticket_number
        assert new_ticket.ticket_url == ticket_url
        assert new_ticket.workspace_dir == workspace_dir

    def test_update_existing_ticket(self):
        # setup
        ticket_number = "DEV-00012"
        ticket_url = "http://devsd"
        workspace_dir = "/Applications/Anchor"
        comments = ["comment 1"]
        t = Ticket(ticket_number=ticket_number, ticket_url=ticket_url, workspace_dir=workspace_dir, ticket_comments=comments)
        existing_ticket = self.app_data.upsert_ticket(ticket_number, t)
        assert existing_ticket is not None

        # changes
        new_ticket_url = "http://newdev.co"
        new_t = Ticket(ticket_number=ticket_number, ticket_url=new_ticket_url)

        # test
        old_ticket: Ticket = self.app_data.upsert_ticket(ticket_number, new_t)

        # assert
        assert old_ticket.ticket_number == ticket_number
        assert old_ticket.ticket_url == new_ticket_url
        assert old_ticket.workspace_dir == workspace_dir
        assert len(old_ticket.ticket_comments) == 1
