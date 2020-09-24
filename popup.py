# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesignV3_Popup.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PreviewWindow(object):
    def setupUi(self, PreviewWindow):
        PreviewWindow.setObjectName("PreviewWindow")
        PreviewWindow.resize(640, 469)
        self.centralwidget = QtWidgets.QWidget(PreviewWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PreviewTable = QtWidgets.QTableWidget(self.centralwidget)
        self.PreviewTable.setGeometry(QtCore.QRect(0, 0, 641, 381))
        self.PreviewTable.setObjectName("PreviewTable")
        self.PreviewTable.setColumnCount(0)
        self.PreviewTable.setRowCount(0)
        self.Savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Savebutton.setGeometry(QtCore.QRect(540, 390, 91, 31))
        self.Savebutton.setObjectName("Savebutton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(10, 390, 91, 31))
        self.ExitButton.setObjectName("ExitButton")
        PreviewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PreviewWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        PreviewWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PreviewWindow)
        self.statusbar.setObjectName("statusbar")
        PreviewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PreviewWindow)
        QtCore.QMetaObject.connectSlotsByName(PreviewWindow)

    def retranslateUi(self, PreviewWindow):
        _translate = QtCore.QCoreApplication.translate
        PreviewWindow.setWindowTitle(_translate("PreviewWindow", "Preview Data"))
        self.Savebutton.setText(_translate("PreviewWindow", "Save"))
        self.ExitButton.setText(_translate("PreviewWindow", "Exit"))

