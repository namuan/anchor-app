import logging
import os

from PyQt5.QtWidgets import QFileDialog

from anchor.core import truncate, abbreviate
from anchor.core.core_settings import app_settings
from anchor.core.git_interactor import git_info, is_git_dir
from anchor.model.app_data import Ticket


class GitStatsPresenter:
    selected_ticket: Ticket

    def __init__(self, parent_view):
        self.selected_ticket = None
        self.parent_view = parent_view
        self.parent_view.btn_workspace.clicked.connect(self.select_directory)
        self.parent_view.btn_create_branch.clicked.connect(self.create_branch)
        app_settings.app_data.signals.ticket_changed.connect(self.refresh)
        app_settings.app_data.signals.branch_changed.connect(self.update_view)
        self.parent_view.btn_create_branch.setEnabled(False)

    def create_branch(self):
        self.parent_view.show_branch_setup_dialog(self.selected_ticket)

    def select_directory(self):
        directory = self.parent_view.open_directory(
            "Select Folder",
            os.path.expandvars("~"),
            QFileDialog.ShowDirsOnly
        )
        if directory:
            print("Adding directory: " + directory)
            app_settings.app_data.add_workspace(self.selected_ticket.ticket_number, directory)

    def refresh(self, ticket: Ticket):
        logging.info(f"Refreshing GitStats for Ticket: {ticket.ticket_number} - Dir: {ticket.workspace_dir}")
        self.selected_ticket = ticket
        self.update_view(ticket.workspace_dir)

    def update_view(self, directory):
        self.parent_view.btn_workspace.setEnabled(self.selected_ticket is not None)
        self.parent_view.btn_create_branch.setEnabled(is_git_dir(self.selected_ticket.workspace_dir))

        if directory:
            viewable_directory = truncate(directory)
            directory_label = f"<a href=\"file://{directory}\">{viewable_directory}</a>"
            self.parent_view.lbl_workspace_dir.setText(directory_label)
            branch, no_changes = git_info(directory)
            self.parent_view.lbl_branch_status.setText(abbreviate(branch, length=25))
            self.parent_view.lbl_pending_changes.setText(f"Pending Changes {no_changes}")
        else:
            self.parent_view.lbl_workspace_dir.setText("select workspace directory 👉")
            self.parent_view.lbl_branch_status.setText("(branch)")
