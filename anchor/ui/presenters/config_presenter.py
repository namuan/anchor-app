import logging
from anchor.core.jira_interactor import JiraInteractor
from anchor.core.core_settings import app_settings


class ConfigPresenter:
    def __init__(self, view, parent_view):
        self.view = view
        self.parent_view = parent_view
        self.jira_interactor = JiraInteractor()
        self.view.initialize()
        self.view.btn_test_jira.pressed.connect(self.jira_connect)
        self.view.btn_save_configuration.pressed.connect(self.on_success)
        self.view.btn_cancel_configuration.pressed.connect(self.ignore_changes)

    def ignore_changes(self):
        self.view.reject()

    def jira_connect(self):
        jira_server = self.view.txt_jira_server.text()
        jira_username = self.view.txt_jira_user.text()
        jira_password = self.view.txt_jira_password.text()

        self.view.lbl_jira_server_status.setText(f"Checking {jira_server}")

        kwargs = {
            'server': jira_server,
            'username': jira_username,
            'password': jira_password,
            'on_success': self.on_test_success,
            'on_failure': self.on_test_failure
        }
        self.jira_interactor.check_connectivity(**kwargs)

    def on_test_success(self, result):
        self.view.lbl_jira_server_status.setText(f"Success")

    def on_test_failure(self, result):
        self.view.lbl_jira_server_status.setText(result.get('message'))

    def on_success(self):
        logging.info("Saving configuration")
        jira_server = self.view.txt_jira_server.text()
        jira_username = self.view.txt_jira_user.text()
        jira_password = self.view.txt_jira_password.text()
        updates_check = self.view.chk_updates_startup.isChecked()
        app_settings.save_configuration(
            jira_server,
            jira_username,
            jira_password,
            updates_check
        )
        self.parent_view.status_bar.showMessage("Ready", 5000)
        self.parent_view.refresh_all_tickets()
        self.view.accept()

    def load_configuration_dialog(self):
        jira_server, jira_user, jira_password = app_settings.load_jira_configuration()
        self.view.txt_jira_server.setText(jira_server)
        self.view.txt_jira_user.setText(jira_user)
        self.view.txt_jira_password.setText(jira_password)
        check_updates = app_settings.load_updates_configuration()
        self.view.chk_updates_startup.setChecked(check_updates)
        self.view.exec()
