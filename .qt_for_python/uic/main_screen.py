# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dzenis Madzovic\OneDrive - Högskolan Kristianstad\Skrivbordet\Projects\GoldApp\src\examples\main_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 389)
        MainWindow.setStyleSheet("background-color: rgb(220, 221, 255);\n"
"border-top-color: rgb(255, 255, 255);\n"
"margin-left: 30px;\n"
"margin-right: 30px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.RoundButton = QtWidgets.QPushButton(self.widget)
        self.RoundButton.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"aspect-ratio: 1 / 1;\n"
" color: white;\n"
" border-width: 0px;\n"
" border-radius:50px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgb(255, 220, 99);\n"
"}")
        self.RoundButton.setObjectName("RoundButton")
        self.horizontalLayout_2.addWidget(self.RoundButton)
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(100, 100))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2.addWidget(self.widget1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"aspect-ratio: 1 / 1;\n"
" color: white;\n"
" border-width: 0px;\n"
" border-radius:50px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgb(255, 220, 99);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"aspect-ratio: 1 / 1;\n"
" color: white;\n"
" border-width: 0px;\n"
" border-radius:50px;\n"
" min-width:100px;\n"
" min-height:100px;\n"
"}\n"
"QPushButton:Hover{\n"
"background-color: rgb(255, 220, 99);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RoundButton.setText(_translate("MainWindow", "Meetings"))
        self.pushButton_2.setText(_translate("MainWindow", "Attributes"))
        self.pushButton_3.setText(_translate("MainWindow", "Assistance"))