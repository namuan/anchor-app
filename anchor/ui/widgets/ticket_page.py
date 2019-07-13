from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def acceptNavigationRequest(self, nav_url, nav_type, is_main_frame):
        QDesktopServices.openUrl(nav_url)
        return False
