from PyQt6.QtWidgets import (QDialog)

from anchor.ui.generated.progress_dialog import Ui_ProgressDialog


class ProgressDialog(QDialog, Ui_ProgressDialog):

    def __init__(self, parent=None):
        super(ProgressDialog, self).__init__(parent)
        self.initialize()

    def initialize(self):
        self.setupUi(self)
        self.setFixedSize(self.size())

    def show_dialog(self, message=""):
        self.lbl_progress_status.setText(message)
        self.show()

    def hide_dialog(self):
        self.lbl_progress_status.setText("")
        self.hide()

    def update_status(self, percent_completed, message):
        self.lbl_progress_status.setValue(percent_completed)
        self.lbl_progress_status.setText(message)
