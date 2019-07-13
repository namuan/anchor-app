from PyQt5.QtWidgets import (QDialog)

from anchor.ui.generated.jira_server_dialog import Ui_Dialog
from anchor.ui.presenters.config_presenter import ConfigPresenter


class JiraConfigurationDialog(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(JiraConfigurationDialog, self).__init__(parent)
        self.presenter = ConfigPresenter(self, parent)

    def initialize(self):
        self.setupUi(self)
        self.setFixedSize(self.size())
        # @todo: Add validator
        # https://snorfalorpagus.net/blog/2014/08/09/validating-user-input-in-pyqt4-using-qvalidator/

    def show_dialog(self):
        self.presenter.load_configuration_dialog()
