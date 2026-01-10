from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication


def file_menu(self):
    """Create a file submenu with an Open File item that opens a file dialog."""
    self.file_sub_menu = self.menu_bar.addMenu('File')

    self.exit_action = QAction('Exit Application', self)
    self.exit_action.setStatusTip('Exit the application.')
    self.exit_action.setShortcut('CTRL+Q')
    self.exit_action.triggered.connect(lambda: QApplication.quit())

    self.file_sub_menu.addAction(self.exit_action)


def help_menu(self):
    """Create a help submenu with an About item."""
    self.help_sub_menu = self.menu_bar.addMenu('Help')

    self.about_action = QAction('About', self)
    self.about_action.setStatusTip('About this application.')
    self.about_action.triggered.connect(lambda: QApplication.aboutQt())

    self.help_sub_menu.addAction(self.about_action)
