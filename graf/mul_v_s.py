# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mul_v_s.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        Dialog.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.title_A_5 = QtWidgets.QLabel(Dialog)
        self.title_A_5.setGeometry(QtCore.QRect(20, 50, 111, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_5.setFont(font)
        self.title_A_5.setObjectName("title_A_5")
        self.title_A_3 = QtWidgets.QLabel(Dialog)
        self.title_A_3.setGeometry(QtCore.QRect(20, 10, 271, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_3.setFont(font)
        self.title_A_3.setObjectName("title_A_3")
        self.lines_A = QtWidgets.QLineEdit(Dialog)
        self.lines_A.setGeometry(QtCore.QRect(170, 50, 121, 20))
        self.lines_A.setObjectName("lines_A")
        self.tableWidget_A = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_A.setGeometry(QtCore.QRect(110, 110, 271, 201))
        self.tableWidget_A.setObjectName("tableWidget_A")
        self.tableWidget_A.setColumnCount(0)
        self.tableWidget_A.setRowCount(0)
        self.title_A = QtWidgets.QLabel(Dialog)
        self.title_A.setGeometry(QtCore.QRect(160, 90, 171, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A.setFont(font)
        self.title_A.setObjectName("title_A")
        self.title_A_6 = QtWidgets.QLabel(Dialog)
        self.title_A_6.setGeometry(QtCore.QRect(10, 340, 151, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_A_6.setFont(font)
        self.title_A_6.setObjectName("title_A_6")
        self.scalar = QtWidgets.QLineEdit(Dialog)
        self.scalar.setGeometry(QtCore.QRect(160, 340, 121, 20))
        self.scalar.setObjectName("scalar")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 330, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ввод значений"))
        self.title_A_5.setText(_translate("Dialog", "Кол-во строк:"))
        self.title_A_3.setText(_translate("Dialog", "Введите размерность вектора:"))
        self.title_A.setText(_translate("Dialog", "Заполните вектор:"))
        self.title_A_6.setText(_translate("Dialog", "Введите скаляр b:"))
        self.pushButton.setText(_translate("Dialog", "Заполнить вектор"))
        self.pushButton_2.setText(_translate("Dialog", "Выполнить операцию"))
