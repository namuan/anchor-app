# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/jira_ticket_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_JiraTicketDialog(object):
    def setupUi(self, JiraTicketDialog):
        JiraTicketDialog.setObjectName("JiraTicketDialog")
        JiraTicketDialog.resize(466, 107)
        JiraTicketDialog.setModal(True)
        self.label = QtWidgets.QLabel(JiraTicketDialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label.setObjectName("label")
        self.txt_jira_ticket = QtWidgets.QLineEdit(JiraTicketDialog)
        self.txt_jira_ticket.setGeometry(QtCore.QRect(90, 30, 361, 21))
        self.txt_jira_ticket.setObjectName("txt_jira_ticket")
        self.btn_ok = QtWidgets.QPushButton(JiraTicketDialog)
        self.btn_ok.setGeometry(QtCore.QRect(340, 60, 113, 32))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(JiraTicketDialog)
        self.btn_cancel.setGeometry(QtCore.QRect(220, 60, 113, 32))
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(JiraTicketDialog)
        QtCore.QMetaObject.connectSlotsByName(JiraTicketDialog)

    def retranslateUi(self, JiraTicketDialog):
        _translate = QtCore.QCoreApplication.translate
        JiraTicketDialog.setWindowTitle(_translate("JiraTicketDialog", "Enter JIRA Ticket"))
        self.label.setText(_translate("JiraTicketDialog", "JIRA Ticket"))
        self.btn_ok.setText(_translate("JiraTicketDialog", "Ok"))
        self.btn_cancel.setText(_translate("JiraTicketDialog", "Cancel"))

