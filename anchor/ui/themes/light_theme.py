import logging
from PyQt5.QtCore import Qt, QFile, QFileInfo, QTextStream
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import QProxyStyle, qApp


class LightTheme(QProxyStyle):
    def __init__(self):
        super(LightTheme, self).__init__()
        palette = qApp.palette()
        palette.setColor(QPalette.Window, QColor(239, 240, 241))
        palette.setColor(QPalette.WindowText, QColor(49, 54, 59))
        palette.setColor(QPalette.Base, QColor(252, 252, 252))
        palette.setColor(QPalette.AlternateBase, QColor(239, 240, 241))
        palette.setColor(QPalette.ToolTipBase, QColor(239, 240, 241))
        palette.setColor(QPalette.ToolTipText, QColor(49, 54, 59))
        palette.setColor(QPalette.Text, QColor(49, 54, 59))
        palette.setColor(QPalette.Button, QColor(239, 240, 241))
        palette.setColor(QPalette.ButtonText, QColor(49, 54, 59))
        palette.setColor(QPalette.BrightText, QColor(255, 255, 255))
        palette.setColor(QPalette.Link, QColor(41, 128, 185))
        palette.setColor(QPalette.Highlight, QColor(126, 71, 130))
        palette.setColor(QPalette.HighlightedText, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.Light, Qt.white)
        palette.setColor(QPalette.Disabled, QPalette.Shadow, QColor(234, 234, 234))
        qApp.setPalette(palette)

    @staticmethod
    def load_stylesheet():
        filename = ":/styles/light.qss"

        if QFileInfo(filename).exists():
            qss_file = QFile(filename)
            qss_file.open(QFile.ReadOnly | QFile.Text)
            content = QTextStream(qss_file).readAll()
            qApp.setStyleSheet(content)
        else:
            logging.error(f"Unable to read light.qss file from {filename}")
