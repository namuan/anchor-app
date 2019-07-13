# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/configuration_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.setWindowModality(QtCore.Qt.WindowModal)
        Configuration.resize(486, 255)
        Configuration.setModal(True)
        self.tabWidget = QtWidgets.QTabWidget(Configuration)
        self.tabWidget.setGeometry(QtCore.QRect(12, 6, 461, 201))
        self.tabWidget.setObjectName("tabWidget")
        self.jira = QtWidgets.QWidget()
        self.jira.setObjectName("jira")
        self.label = QtWidgets.QLabel(self.jira)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.txt_jira_server = QtWidgets.QLineEdit(self.jira)
        self.txt_jira_server.setGeometry(QtCore.QRect(90, 20, 351, 21))
        self.txt_jira_server.setObjectName("txt_jira_server")
        self.label_2 = QtWidgets.QLabel(self.jira)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.jira)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.txt_jira_user = QtWidgets.QLineEdit(self.jira)
        self.txt_jira_user.setGeometry(QtCore.QRect(90, 60, 351, 21))
        self.txt_jira_user.setObjectName("txt_jira_user")
        self.txt_jira_password = QtWidgets.QLineEdit(self.jira)
        self.txt_jira_password.setGeometry(QtCore.QRect(90, 100, 351, 21))
        self.txt_jira_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_jira_password.setObjectName("txt_jira_password")
        self.btn_test_jira = QtWidgets.QPushButton(self.jira)
        self.btn_test_jira.setGeometry(QtCore.QRect(330, 130, 113, 32))
        self.btn_test_jira.setObjectName("btn_test_jira")
        self.lbl_jira_server_status = QtWidgets.QLabel(self.jira)
        self.lbl_jira_server_status.setGeometry(QtCore.QRect(90, 130, 231, 30))
        self.lbl_jira_server_status.setText("")
        self.lbl_jira_server_status.setObjectName("lbl_jira_server_status")
        self.tabWidget.addTab(self.jira, "")
        self.update = QtWidgets.QWidget()
        self.update.setObjectName("update")
        self.chk_updates_startup = QtWidgets.QCheckBox(self.update)
        self.chk_updates_startup.setGeometry(QtCore.QRect(20, 20, 221, 20))
        self.chk_updates_startup.setChecked(True)
        self.chk_updates_startup.setObjectName("chk_updates_startup")
        self.tabWidget.addTab(self.update, "")
        self.btn_save_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_save_configuration.setGeometry(QtCore.QRect(360, 210, 113, 32))
        self.btn_save_configuration.setObjectName("btn_save_configuration")
        self.btn_cancel_configuration = QtWidgets.QPushButton(Configuration)
        self.btn_cancel_configuration.setGeometry(QtCore.QRect(250, 210, 113, 32))
        self.btn_cancel_configuration.setObjectName("btn_cancel_configuration")

        self.retranslateUi(Configuration)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Settings"))
        self.label.setText(_translate("Configuration", "JIRA Server"))
        self.label_2.setText(_translate("Configuration", "user"))
        self.label_3.setText(_translate("Configuration", "password"))
        self.btn_test_jira.setText(_translate("Configuration", "Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.jira), _translate("Configuration", "JIRA"))
        self.chk_updates_startup.setText(_translate("Configuration", "Check for updates on start up"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.update), _translate("Configuration", "Updates"))
        self.btn_save_configuration.setText(_translate("Configuration", "OK"))
        self.btn_cancel_configuration.setText(_translate("Configuration", "Cancel"))

