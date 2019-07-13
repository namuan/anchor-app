# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/feature_branch_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FeatureBranchDialog(object):
    def setupUi(self, FeatureBranchDialog):
        FeatureBranchDialog.setObjectName("FeatureBranchDialog")
        FeatureBranchDialog.setWindowModality(QtCore.Qt.WindowModal)
        FeatureBranchDialog.resize(475, 318)
        FeatureBranchDialog.setModal(True)
        self.btn_create_branch = QtWidgets.QPushButton(FeatureBranchDialog)
        self.btn_create_branch.setGeometry(QtCore.QRect(350, 280, 113, 31))
        self.btn_create_branch.setObjectName("btn_create_branch")
        self.btn_cancel_create_branch = QtWidgets.QPushButton(FeatureBranchDialog)
        self.btn_cancel_create_branch.setGeometry(QtCore.QRect(230, 280, 113, 30))
        self.btn_cancel_create_branch.setObjectName("btn_cancel_create_branch")
        self.txt_main_branch = QtWidgets.QLineEdit(FeatureBranchDialog)
        self.txt_main_branch.setGeometry(QtCore.QRect(140, 148, 321, 21))
        self.txt_main_branch.setText("")
        self.txt_main_branch.setObjectName("txt_main_branch")
        self.label = QtWidgets.QLabel(FeatureBranchDialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 431, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_2.setGeometry(QtCore.QRect(60, 40, 391, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_3.setGeometry(QtCore.QRect(60, 60, 391, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_4.setGeometry(QtCore.QRect(60, 80, 391, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_5.setGeometry(QtCore.QRect(20, 148, 111, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_6.setGeometry(QtCore.QRect(20, 188, 111, 20))
        self.label_6.setObjectName("label_6")
        self.txt_feature_branch = QtWidgets.QLineEdit(FeatureBranchDialog)
        self.txt_feature_branch.setGeometry(QtCore.QRect(140, 188, 321, 21))
        self.txt_feature_branch.setObjectName("txt_feature_branch")
        self.lbl_error = QtWidgets.QLabel(FeatureBranchDialog)
        self.lbl_error.setGeometry(QtCore.QRect(20, 258, 441, 16))
        self.lbl_error.setObjectName("lbl_error")
        self.chk_apply_stash = QtWidgets.QCheckBox(FeatureBranchDialog)
        self.chk_apply_stash.setGeometry(QtCore.QRect(140, 228, 221, 20))
        self.chk_apply_stash.setChecked(True)
        self.chk_apply_stash.setObjectName("chk_apply_stash")
        self.label_7 = QtWidgets.QLabel(FeatureBranchDialog)
        self.label_7.setGeometry(QtCore.QRect(60, 99, 391, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(FeatureBranchDialog)
        QtCore.QMetaObject.connectSlotsByName(FeatureBranchDialog)
        FeatureBranchDialog.setTabOrder(self.txt_main_branch, self.txt_feature_branch)
        FeatureBranchDialog.setTabOrder(self.txt_feature_branch, self.chk_apply_stash)
        FeatureBranchDialog.setTabOrder(self.chk_apply_stash, self.btn_cancel_create_branch)
        FeatureBranchDialog.setTabOrder(self.btn_cancel_create_branch, self.btn_create_branch)

    def retranslateUi(self, FeatureBranchDialog):
        _translate = QtCore.QCoreApplication.translate
        FeatureBranchDialog.setWindowTitle(_translate("FeatureBranchDialog", "Create new branch"))
        self.btn_create_branch.setText(_translate("FeatureBranchDialog", "OK"))
        self.btn_cancel_create_branch.setText(_translate("FeatureBranchDialog", "Cancel"))
        self.label.setText(_translate("FeatureBranchDialog", "Creates new feature branch"))
        self.label_2.setText(_translate("FeatureBranchDialog", "- Stash all changes in the current branch"))
        self.label_3.setText(_translate("FeatureBranchDialog", "- Checks out main branch (As shown and can be changed)"))
        self.label_4.setText(_translate("FeatureBranchDialog", "- Creates and checks out new branch"))
        self.label_5.setText(_translate("FeatureBranchDialog", "Main branch"))
        self.label_6.setText(_translate("FeatureBranchDialog", "Feature branch"))
        self.lbl_error.setText(_translate("FeatureBranchDialog", "Error message"))
        self.chk_apply_stash.setText(_translate("FeatureBranchDialog", "Apply Stash on new branch"))
        self.label_7.setText(_translate("FeatureBranchDialog", "- Apply Stash (If selected)"))

