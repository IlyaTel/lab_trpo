# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two_scalar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 150)
        Dialog.setMinimumSize(QtCore.QSize(500, 150))
        Dialog.setMaximumSize(QtCore.QSize(500, 150))
        Dialog.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.title_A_3 = QtWidgets.QLabel(Dialog)
        self.title_A_3.setGeometry(QtCore.QRect(20, 10, 451, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_3.setFont(font)
        self.title_A_3.setObjectName("title_A_3")
        self.title_A_6 = QtWidgets.QLabel(Dialog)
        self.title_A_6.setGeometry(QtCore.QRect(20, 50, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_6.setFont(font)
        self.title_A_6.setObjectName("title_A_6")
        self.scalar = QtWidgets.QLineEdit(Dialog)
        self.scalar.setGeometry(QtCore.QRect(180, 50, 121, 20))
        self.scalar.setObjectName("scalar")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 50, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scalar_2 = QtWidgets.QLineEdit(Dialog)
        self.scalar_2.setGeometry(QtCore.QRect(180, 80, 121, 20))
        self.scalar_2.setObjectName("scalar_2")
        self.title_A_7 = QtWidgets.QLabel(Dialog)
        self.title_A_7.setGeometry(QtCore.QRect(20, 80, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_7.setFont(font)
        self.title_A_7.setObjectName("title_A_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ошибка"))
        self.title_A_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Введите скаляры:</p></body></html>"))
        self.title_A_6.setText(_translate("Dialog", "Введите скаляр a:"))
        self.pushButton_2.setText(_translate("Dialog", "Выполнить операцию"))
        self.title_A_7.setText(_translate("Dialog", "Введите скаляр b:"))
