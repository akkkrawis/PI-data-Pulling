# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mydesignV3.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(779, 684)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(779, 684))
        MainWindow.setMaximumSize(QtCore.QSize(779, 684))
        MainWindow.setBaseSize(QtCore.QSize(800, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 120, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(140, 180, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(100, 120, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(540, 120, 194, 22))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 600, 91, 31))
        self.pushButton2.setObjectName("pushButton2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 180, 301, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.Server = QtWidgets.QComboBox(self.centralwidget)
        self.Server.setGeometry(QtCore.QRect(100, 90, 191, 22))
        self.Server.setObjectName("Server")
        self.Machine = QtWidgets.QComboBox(self.centralwidget)
        self.Machine.setGeometry(QtCore.QRect(540, 90, 191, 22))
        self.Machine.setObjectName("Machine")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 90, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 150, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.Try = QtWidgets.QPushButton(self.centralwidget)
        self.Try.setGeometry(QtCore.QRect(560, 600, 91, 31))
        self.Try.setObjectName("Try")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 150, 91, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 220, 751, 371))
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 741, 341))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 441, 341))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.CriteriaBox = QtWidgets.QComboBox(self.tab_2)
        self.CriteriaBox.setGeometry(QtCore.QRect(550, 90, 171, 22))
        self.CriteriaBox.setObjectName("CriteriaBox")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(470, 90, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Value2 = QtWidgets.QLineEdit(self.tab_2)
        self.Value2.setGeometry(QtCore.QRect(650, 130, 71, 22))
        self.Value2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Value2.setObjectName("Value2")
        self.VariableBox = QtWidgets.QComboBox(self.tab_2)
        self.VariableBox.setGeometry(QtCore.QRect(550, 50, 171, 22))
        self.VariableBox.setMouseTracking(False)
        self.VariableBox.setObjectName("VariableBox")
        self.SDCheck = QtWidgets.QCheckBox(self.tab_2)
        self.SDCheck.setGeometry(QtCore.QRect(470, 200, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SDCheck.setFont(font)
        self.SDCheck.setObjectName("SDCheck")
        self.AvgCheck = QtWidgets.QCheckBox(self.tab_2)
        self.AvgCheck.setGeometry(QtCore.QRect(470, 170, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AvgCheck.setFont(font)
        self.AvgCheck.setObjectName("AvgCheck")
        self.Value1 = QtWidgets.QLineEdit(self.tab_2)
        self.Value1.setGeometry(QtCore.QRect(550, 130, 71, 22))
        self.Value1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Value1.setObjectName("Value1")
        self.FilterCheck = QtWidgets.QCheckBox(self.tab_2)
        self.FilterCheck.setGeometry(QtCore.QRect(670, 270, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FilterCheck.setFont(font)
        self.FilterCheck.setObjectName("FilterCheck")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(470, 50, 81, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(470, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(620, 130, 31, 21))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.FilRun = QtWidgets.QPushButton(self.tab_2)
        self.FilRun.setEnabled(True)
        self.FilRun.setGeometry(QtCore.QRect(470, 300, 91, 31))
        self.FilRun.setObjectName("FilRun")
        self.AvgNum = QtWidgets.QLCDNumber(self.tab_2)
        self.AvgNum.setEnabled(True)
        self.AvgNum.setGeometry(QtCore.QRect(550, 170, 71, 23))
        self.AvgNum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.AvgNum.setProperty("value", 0.0)
        self.AvgNum.setProperty("intValue", 0)
        self.AvgNum.setObjectName("AvgNum")
        self.SDNum = QtWidgets.QLCDNumber(self.tab_2)
        self.SDNum.setGeometry(QtCore.QRect(550, 200, 71, 23))
        self.SDNum.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.SDNum.setObjectName("SDNum")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(470, 10, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(670, 310, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.GraphShow = QtWidgets.QPushButton(self.tab_2)
        self.GraphShow.setEnabled(True)
        self.GraphShow.setGeometry(QtCore.QRect(470, 260, 91, 31))
        self.GraphShow.setObjectName("GraphShow")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 741, 301))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(10)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        self.MulFilRun = QtWidgets.QPushButton(self.tab_3)
        self.MulFilRun.setEnabled(True)
        self.MulFilRun.setGeometry(QtCore.QRect(650, 310, 91, 31))
        self.MulFilRun.setObjectName("MulFilRun")
        self.DropNa = QtWidgets.QCheckBox(self.tab_3)
        self.DropNa.setGeometry(QtCore.QRect(550, 309, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DropNa.setFont(font)
        self.DropNa.setObjectName("DropNa")
        self.Outlier = QtWidgets.QCheckBox(self.tab_3)
        self.Outlier.setGeometry(QtCore.QRect(470, 309, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Outlier.setFont(font)
        self.Outlier.setObjectName("Outlier")
        self.tabWidget.addTab(self.tab_3, "")
        self.Savebutton = QtWidgets.QPushButton(self.centralwidget)
        self.Savebutton.setGeometry(QtCore.QRect(680, 600, 91, 31))
        self.Savebutton.setObjectName("Savebutton")
        self.Try_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Try_2.setEnabled(True)
        self.Try_2.setGeometry(QtCore.QRect(20, 180, 91, 31))
        self.Try_2.setObjectName("Try_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 150, 401, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Spanlist = QtWidgets.QComboBox(self.centralwidget)
        self.Spanlist.setGeometry(QtCore.QRect(540, 150, 91, 22))
        self.Spanlist.setObjectName("Spanlist")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(530, 20, 201, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Capture.JPG"))
        self.label_8.setObjectName("label_8")
        self.BrownFile = QtWidgets.QPushButton(self.centralwidget)
        self.BrownFile.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.BrownFile.setObjectName("BrownFile")
        self.fliepath = QtWidgets.QLabel(self.centralwidget)
        self.fliepath.setGeometry(QtCore.QRect(120, 50, 401, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.fliepath.setFont(font)
        self.fliepath.setAutoFillBackground(False)
        self.fliepath.setText("")
        self.fliepath.setOpenExternalLinks(False)
        self.fliepath.setObjectName("fliepath")
        self.GenGraph = QtWidgets.QPushButton(self.centralwidget)
        self.GenGraph.setGeometry(QtCore.QRect(450, 600, 91, 31))
        self.GenGraph.setObjectName("GenGraph")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(630, 640, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setScaledContents(False)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 640, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Start Time"))
        self.label_2.setText(_translate("MainWindow", "End Time"))
        self.label_3.setText(_translate("MainWindow", "PI TAG PULLING PROGRAM "))
        self.pushButton.setText(_translate("MainWindow", "Run"))
        self.pushButton2.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "SERVER"))
        self.label_6.setText(_translate("MainWindow", "MACHINE"))
        self.label_7.setText(_translate("MainWindow", "Span Time"))
        self.Try.setText(_translate("MainWindow", "Try"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Check"))
        self.label_10.setText(_translate("MainWindow", "Criteria"))
        self.Value2.setText(_translate("MainWindow", "0"))
        self.SDCheck.setText(_translate("MainWindow", "SD"))
        self.AvgCheck.setText(_translate("MainWindow", "Average"))
        self.Value1.setText(_translate("MainWindow", "0"))
        self.FilterCheck.setText(_translate("MainWindow", "Single"))
        self.label_9.setText(_translate("MainWindow", "Variable"))
        self.label_12.setText(_translate("MainWindow", "Value"))
        self.label_13.setText(_translate("MainWindow", "To"))
        self.FilRun.setText(_translate("MainWindow", "Filter Run"))
        self.label_11.setText(_translate("MainWindow", "----- Filter Mode -----"))
        self.radioButton.setText(_translate("MainWindow", "Single"))
        self.GraphShow.setText(_translate("MainWindow", "Show Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Use"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tag Name"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Criteria"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sign"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Value1"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Value2"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Average"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "SD"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Graph"))
        self.MulFilRun.setText(_translate("MainWindow", "Filter Save"))
        self.DropNa.setText(_translate("MainWindow", "Drop Text"))
        self.Outlier.setText(_translate("MainWindow", "Outlier"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Multi Filter"))
        self.Savebutton.setText(_translate("MainWindow", "Save"))
        self.Try_2.setText(_translate("MainWindow", "Check"))
        self.BrownFile.setText(_translate("MainWindow", "Browse Tag file"))
        self.GenGraph.setText(_translate("MainWindow", "Graph"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#d0d0d0;\">Created by : Jam PPDC</span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#b5b5b5;\">Version 0.7</span></p></body></html>"))