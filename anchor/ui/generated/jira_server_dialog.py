# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/jira_server_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(528, 222)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.txt_jira_password = QtWidgets.QLineEdit(Dialog)
        self.txt_jira_password.setText("")
        self.txt_jira_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_jira_password.setObjectName("txt_jira_password")
        self.gridLayout.addWidget(self.txt_jira_password, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txt_jira_server = QtWidgets.QLineEdit(Dialog)
        self.txt_jira_server.setObjectName("txt_jira_server")
        self.gridLayout.addWidget(self.txt_jira_server, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_test = QtWidgets.QPushButton(Dialog)
        self.btn_test.setObjectName("btn_test")
        self.horizontalLayout.addWidget(self.btn_test)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.txt_jira_username = QtWidgets.QLineEdit(Dialog)
        self.txt_jira_username.setObjectName("txt_jira_username")
        self.gridLayout.addWidget(self.txt_jira_username, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "JIRA Server configuration"))
        self.label.setText(_translate("Dialog", "JIRA Server"))
        self.label_2.setText(_translate("Dialog", "Username"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.btn_test.setText(_translate("Dialog", "Test And Save"))

