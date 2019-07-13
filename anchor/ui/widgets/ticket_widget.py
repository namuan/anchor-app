from PyQt5 import QtWidgets, QtGui

from anchor.core import abbreviate


class TicketWidget(QtWidgets.QWidget):
    url: str

    def __init__(self, parent=None):
        super(TicketWidget, self).__init__(parent)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.top_row_layout = QtWidgets.QHBoxLayout()

        self.lbl_icon = QtWidgets.QLabel()
        self.lbl_ticket_number = QtWidgets.QLabel()
        self.lbl_ticket_status = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_ticket_status.setFont(font)
        self.lbl_ticket_status.setFlat(True)
        self.lbl_ticket_status.setDisabled(True)
        self.lbl_ticket_status.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        self.lbl_ticket_status.setStyleSheet('''
            QPushButton {
                padding: -5px;
            }
        ''')
        self.lbl_ticket_title = QtWidgets.QLabel()
        self.lbl_icon.setPixmap(QtGui.QPixmap(":/images/notifier-48.png"))

        self.top_row_layout.addWidget(self.lbl_icon)
        self.top_row_layout.addWidget(self.lbl_ticket_number)
        self.top_row_layout.addWidget(self.lbl_ticket_status)

        self.vertical_layout.addLayout(self.top_row_layout)
        self.vertical_layout.addWidget(self.lbl_ticket_title)

        self.setLayout(self.vertical_layout)

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_ticket_number.setFont(font)

    def set_data(self, ticket_number, ticket_status, ticket_title, url):
        self.lbl_ticket_number.setText(ticket_number)
        self.lbl_ticket_status.setText(ticket_status)
        self.lbl_ticket_title.setText(abbreviate(ticket_title))
        self.url = url
        self.setToolTip(ticket_title)

    def get_data(self):
        return self.lbl_ticket_number.text(), self.lbl_ticket_title.text(), self.url
