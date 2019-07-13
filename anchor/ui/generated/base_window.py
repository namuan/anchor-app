# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/base_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 728)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 5, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_ticket_title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_ticket_title.sizePolicy().hasHeightForWidth())
        self.lbl_ticket_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_ticket_title.setFont(font)
        self.lbl_ticket_title.setLineWidth(1)
        self.lbl_ticket_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_ticket_title.setOpenExternalLinks(True)
        self.lbl_ticket_title.setObjectName("lbl_ticket_title")
        self.horizontalLayout_3.addWidget(self.lbl_ticket_title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btn_copy_ticket = QtWidgets.QToolButton(self.centralwidget)
        self.btn_copy_ticket.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/copy-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_copy_ticket.setIcon(icon)
        self.btn_copy_ticket.setObjectName("btn_copy_ticket")
        self.horizontalLayout_3.addWidget(self.btn_copy_ticket)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.list_apps = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_apps.sizePolicy().hasHeightForWidth())
        self.list_apps.setSizePolicy(sizePolicy)
        self.list_apps.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_apps.setObjectName("list_apps")
        self.gridLayout.addWidget(self.list_apps, 6, 5, 4, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_connect_source = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_connect_source.sizePolicy().hasHeightForWidth())
        self.lbl_connect_source.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_connect_source.setFont(font)
        self.lbl_connect_source.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lbl_connect_source.setObjectName("lbl_connect_source")
        self.verticalLayout_2.addWidget(self.lbl_connect_source)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_workspace_dir = QtWidgets.QLabel(self.centralwidget)
        self.lbl_workspace_dir.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lbl_workspace_dir.setText("")
        self.lbl_workspace_dir.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_workspace_dir.setOpenExternalLinks(True)
        self.lbl_workspace_dir.setObjectName("lbl_workspace_dir")
        self.horizontalLayout.addWidget(self.lbl_workspace_dir)
        self.btn_workspace = QtWidgets.QToolButton(self.centralwidget)
        self.btn_workspace.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/folder-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_workspace.setIcon(icon1)
        self.btn_workspace.setAutoRaise(False)
        self.btn_workspace.setObjectName("btn_workspace")
        self.horizontalLayout.addWidget(self.btn_workspace)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lbl_branch_status = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_branch_status.sizePolicy().hasHeightForWidth())
        self.lbl_branch_status.setSizePolicy(sizePolicy)
        self.lbl_branch_status.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lbl_branch_status.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_branch_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_branch_status.setObjectName("lbl_branch_status")
        self.verticalLayout_2.addWidget(self.lbl_branch_status)
        self.lbl_pending_changes = QtWidgets.QLabel(self.centralwidget)
        self.lbl_pending_changes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_pending_changes.setObjectName("lbl_pending_changes")
        self.verticalLayout_2.addWidget(self.lbl_pending_changes)
        self.btn_create_branch = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create_branch.setObjectName("btn_create_branch")
        self.verticalLayout_2.addWidget(self.btn_create_branch)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.lbl_move_tickets = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_move_tickets.setFont(font)
        self.lbl_move_tickets.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_move_tickets.setObjectName("lbl_move_tickets")
        self.verticalLayout_2.addWidget(self.lbl_move_tickets)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 5, 2, 1)
        self.lbl_apps = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_apps.setFont(font)
        self.lbl_apps.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_apps.setObjectName("lbl_apps")
        self.gridLayout.addWidget(self.lbl_apps, 5, 5, 1, 1)
        self.btn_add_application = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_application.setObjectName("btn_add_application")
        self.gridLayout.addWidget(self.btn_add_application, 10, 5, 1, 1)
        self.web_engine = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.web_engine.setObjectName("web_engine")
        self.gridLayout.addWidget(self.web_engine, 1, 1, 8, 1)
        self.txt_ticket_notes = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_ticket_notes.sizePolicy().hasHeightForWidth())
        self.txt_ticket_notes.setSizePolicy(sizePolicy)
        self.txt_ticket_notes.setObjectName("txt_ticket_notes")
        self.gridLayout.addWidget(self.txt_ticket_notes, 9, 1, 2, 1)
        self.tickets_list_widget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tickets_list_widget.sizePolicy().hasHeightForWidth())
        self.tickets_list_widget.setSizePolicy(sizePolicy)
        self.tickets_list_widget.setObjectName("tickets_list_widget")
        self.gridLayout.addWidget(self.tickets_list_widget, 0, 0, 11, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_ticket_title.setText(_translate("MainWindow", "Select Ticket"))
        self.btn_copy_ticket.setText(_translate("MainWindow", "..."))
        self.lbl_connect_source.setText(_translate("MainWindow", "Git"))
        self.btn_workspace.setText(_translate("MainWindow", "..."))
        self.lbl_branch_status.setText(_translate("MainWindow", "Branch Status"))
        self.lbl_pending_changes.setText(_translate("MainWindow", "Pending Changes"))
        self.btn_create_branch.setText(_translate("MainWindow", "Create Branch"))
        self.lbl_move_tickets.setText(_translate("MainWindow", "Move to ..."))
        self.lbl_apps.setText(_translate("MainWindow", "Applications"))
        self.btn_add_application.setText(_translate("MainWindow", "Add Application"))
        self.txt_ticket_notes.setPlaceholderText(_translate("MainWindow", "Add your notes here ..."))

from PyQt5 import QtWebEngineWidgets
import resources_rc
