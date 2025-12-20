import logging
import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import QStandardPaths, QDir

from anchor.ui.updater_dialog import Updater
from anchor.ui.widgets.ticket_widget import TicketWidget


class TicketListWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(TicketListWindow, self).__init__(parent)
        self.updater = Updater(self)
        self.ticket_list = QtWidgets.QListWidget(self)
        self.ticket_list.setAlternatingRowColors(True)
        self.ticket_list.setStyleSheet("QListWidget::item:hover{\n"
                                       "    background-color:   rgb(47, 175, 178);\n"
                                       "}")
        # self.ticket_list_presenter = TicketsListPresenter(self.ticket_list, self)
        data = [
            ('TECH-1', 'Ready for development', 'First ticket', 'http://ticket-1'),
            ('TECH-2', 'Ready for refinement', 'Second ticket', 'http://ticket-2')
        ]
        for number, status, title, url in data:
            ticket_widget = TicketWidget(self)
            ticket_widget.set_data(number, status, title, url)
            ticket_widget_item = QtWidgets.QListWidgetItem(self.ticket_list)
            ticket_widget_item.setSizeHint(ticket_widget.sizeHint())

            self.ticket_list.addItem(ticket_widget_item)
            self.ticket_list.setItemWidget(ticket_widget_item, ticket_widget)

        self.ticket_list.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.ticket_list.doubleClicked.connect(self.on_double_clicked)
        self.setCentralWidget(self.ticket_list)

    def on_double_clicked(self):
        self.updater.check()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = TicketListWindow()
    window.show()
    sys.exit(app.exec())
