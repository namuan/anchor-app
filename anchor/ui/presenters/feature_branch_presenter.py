from anchor.core.core_settings import app_settings
from anchor.core.git_interactor import create_feature_branch, apply_stash, git_info
from anchor.model.app_data import Ticket


class FeatureBranchPresenter:
    selected_ticket: Ticket

    def __init__(self, view, parent_view):
        self.view = view
        self.parent_view = parent_view
        self.selected_ticket = None
        self.view.btn_create_branch.pressed.connect(self.on_create_branch)
        self.view.btn_cancel_create_branch.pressed.connect(self.view.reject)

    def load_dialog(self, selected_ticket):
        self.selected_ticket = selected_ticket
        self.view.txt_main_branch.setText("develop")
        branch_prefix = f"{self.selected_ticket.ticket_number}-"
        self.view.txt_feature_branch.setText(branch_prefix)
        self.view.lbl_error.setText("")
        _, changes = git_info(self.selected_ticket.workspace_dir)
        self.view.chk_apply_stash.setChecked(changes > 0)
        self.view.chk_apply_stash.setEnabled(changes > 0)
        self.view.show()

    def apply_stash_checked(self):
        return self.view.chk_apply_stash.isChecked()

    def on_create_branch(self):
        if not self.selected_ticket:
            return

        old_branch = self.view.txt_main_branch.text()
        new_branch = self.view.txt_feature_branch.text()
        workspace_dir = self.selected_ticket.workspace_dir
        try:
            create_feature_branch(workspace_dir, old_branch, new_branch)
            if self.apply_stash_checked():
                apply_stash(workspace_dir)
            app_settings.app_data.update_branch(workspace_dir)
            self.view.accept()
        except IndexError as e:
            self.view.lbl_error.setText(f"ERROR: {e}")
