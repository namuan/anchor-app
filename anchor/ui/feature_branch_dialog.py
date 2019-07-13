from PyQt5.QtWidgets import (QDialog)

from anchor.ui.generated.feature_branch_dialog import Ui_FeatureBranchDialog
from anchor.ui.presenters import FeatureBranchPresenter


class FeatureBranchDialog(QDialog, Ui_FeatureBranchDialog):

    def __init__(self, parent=None):
        super(FeatureBranchDialog, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.presenter = FeatureBranchPresenter(self, parent)

    def show_dialog(self, selected_ticket):
        self.presenter.load_dialog(selected_ticket)
