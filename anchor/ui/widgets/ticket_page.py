from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWebEngineCore import QWebEnginePage


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def acceptNavigationRequest(self, url, type, isMainFrame):
        url_str = url.toString()
        if url_str.startswith('data:'):
            if type == QWebEnginePage.NavigationType.NavigationTypeOther:
                return True
            else:
                return False
        QDesktopServices.openUrl(url)
        return False
