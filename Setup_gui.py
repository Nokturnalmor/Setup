# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\Python\Setup\Setup_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 469)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbtn_ust = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_ust.setFont(font)
        self.rbtn_ust.setObjectName("rbtn_ust")
        self.horizontalLayout.addWidget(self.rbtn_ust)
        self.rbtn_reload = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rbtn_reload.setFont(font)
        self.rbtn_reload.setObjectName("rbtn_reload")
        self.horizontalLayout.addWidget(self.rbtn_reload)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tbl_spis_prog = QtWidgets.QTableWidget(self.groupBox_2)
        self.tbl_spis_prog.setObjectName("tbl_spis_prog")
        self.tbl_spis_prog.setColumnCount(0)
        self.tbl_spis_prog.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tbl_spis_prog)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_putust = QtWidgets.QLineEdit(self.groupBox_3)
        self.le_putust.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.le_putust.setFont(font)
        self.le_putust.setObjectName("le_putust")
        self.horizontalLayout_2.addWidget(self.le_putust)
        self.btn_tool = QtWidgets.QToolButton(self.groupBox_3)
        self.btn_tool.setMinimumSize(QtCore.QSize(33, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_tool.setFont(font)
        self.btn_tool.setObjectName("btn_tool")
        self.horizontalLayout_2.addWidget(self.btn_tool)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.btn_ok = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ok.setMinimumSize(QtCore.QSize(0, 33))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "??????????"))
        self.rbtn_ust.setText(_translate("MainWindow", "??????????????????"))
        self.rbtn_reload.setText(_translate("MainWindow", "????????????????????"))
        self.groupBox_2.setTitle(_translate("MainWindow", "?????????? ????????????????"))
        self.groupBox_3.setTitle(_translate("MainWindow", "???????? ????????????????"))
        self.btn_tool.setText(_translate("MainWindow", "..."))
        self.btn_ok.setText(_translate("MainWindow", "????"))
