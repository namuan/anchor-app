import logging
import logging.handlers
from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication
from pathlib import Path
from tinydb import TinyDB
from typing import Any, Union

from anchor.core import str_to_bool, rot13, tor31
from anchor.model.app_data import AppData


class CoreSettings:

    def __init__(self):
        self.settings: QSettings = None
        self.app_name: str = None
        self.app_dir: Union[Path, Any] = None
        self.app_data: AppData = None

    def init(self):
        if self.settings is None:
            self.app_name = QApplication.applicationName().lower()
            self.app_dir = Path().home().joinpath('Library').joinpath('Preferences').joinpath(self.app_name)
            self.app_dir.mkdir(exist_ok=True)
            settings_file = f"{self.app_name}.ini"
            self.settings = QSettings(self.app_dir.joinpath(settings_file).as_posix(), QSettings.Format.IniFormat)
            self.settings.sync()

    def init_logger(self):
        log_file = f"{self.app_name}.log"
        handlers = [
            logging.handlers.RotatingFileHandler(
                self.app_dir.joinpath(log_file),
                maxBytes=1000000, backupCount=1
            ),
            logging.StreamHandler()
        ]

        logging.basicConfig(
            handlers=handlers,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG
        )
        logging.captureWarnings(capture=True)

    def init_app_data(self, file="app.json"):
        data_location = app_settings.app_dir.joinpath(file)
        db = TinyDB(data_location)
        self.app_data = AppData(db=db)

    def save_window_state(self, geometry, window_state):
        self.settings.setValue('geometry', geometry)
        self.settings.setValue('windowState', window_state)
        self.settings.sync()

    def save_configuration(self, jira_server, jira_username, jira_password, updates_check, jira_jql):
        self.settings.setValue('server', jira_server)
        self.settings.setValue('username', jira_username)
        self.settings.setValue('password', rot13(jira_password))
        self.settings.setValue('startupCheck', updates_check)
        self.settings.setValue('jql', jira_jql)
        self.settings.sync()

    def load_jira_configuration(self):
        default_jql = 'project = FRN AND status IN (New, Ready, "In Progress") AND type IN (Story, Bug)'
        return \
            self.settings.value("server", ""), \
            self.settings.value("username", ""), \
            tor31(self.settings.value("password", "")), \
            self.settings.value("jql", default_jql)

    def load_updates_configuration(self):
        return str_to_bool(self.settings.value("startupCheck", True))

    def jira_configured(self):
        return self.settings.value("server", None) and self.settings.value("username", None) and self.settings.value(
            "password", None)

    def geometry(self):
        return self.settings.value("geometry", None)

    def window_state(self):
        return self.settings.value("windowState", None)


app_settings = CoreSettings()
