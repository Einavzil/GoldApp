# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow_dz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 395)
        MainWindow.setMinimumSize(QtCore.QSize(1800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1800, 1200))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: rgb(220, 221, 255);\n"
            "border-top-color: rgb(255, 255, 255);\n"
            "margin-left: 30px;\n"
            "margin-right: 30px;"
        )
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.login_button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet(
            "QPushButton{\n"
            "background-color:  rgb(255, 203, 99);\n"
            "border: none;\n"
            "border-radius: 10px;\n"
            "color: white;\n"
            "padding: 15px 32px;\n"
            "text-align: center;\n"
            "text-decoration: none;\n"
            "display: inline-block;\n"
            "font-size: 16px;\n"
            "margin-top: 10px;\n"
            "margin-bottom: 10px;\n"
            "margin-left: 600px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:  rgb(255, 220, 99);\n"
            "}"
        )
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 2, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.new_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.new_label.setFont(font)
        self.new_label.setStyleSheet("padding-top: 2cm")
        self.new_label.setObjectName("new_label")
        self.verticalLayout_4.addWidget(
            self.new_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom
        )
        self.new_button = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.new_button.setFont(font)
        self.new_button.setStyleSheet(
            "QPushButton{\n"
            "background-color:  rgb(255, 203, 99);\n"
            "border: none;\n"
            "border-radius: 10px;\n"
            "color: white;\n"
            "padding: 15px 32px;\n"
            "text-align: center;\n"
            "text-decoration: none;\n"
            "display: inline-block;\n"
            "font-size: 16px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:  rgb(255, 220, 99);\n"
            "}"
        )
        self.new_button.setObjectName("new_button")
        self.verticalLayout_4.addWidget(self.new_button)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.email_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("")
        self.email_label.setObjectName("email_label")
        self.verticalLayout_2.addWidget(self.email_label, 0, QtCore.Qt.AlignHCenter)
        self.pw_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pw_label.setFont(font)
        self.pw_label.setObjectName("pw_label")
        self.verticalLayout_2.addWidget(
            self.pw_label, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.inputBox_2 = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inputBox_2.setFont(font)
        self.inputBox_2.setStyleSheet(
            "QLineEdit{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: solid #000;\n"
            "border-width: 0 1px;\n"
            "border-color:  rgb(255, 203, 99);\n"
            "border-radius: 5px;\n"
            "}"
        )
        self.inputBox_2.setText("")
        self.inputBox_2.setObjectName("inputBox_2")
        self.verticalLayout.addWidget(self.inputBox_2)
        self.inputBox = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inputBox.setFont(font)
        self.inputBox.setStyleSheet(
            "QLineEdit{\n"
            "background-color: rgb(255, 255, 255);\n"
            "border: solid #000;\n"
            "border-width: 0 1px;\n"
            "border-color:  rgb(255, 203, 99);\n"
            "border-radius: 5px;\n"
            "}"
        )
        self.inputBox.setText("")
        self.inputBox.setObjectName("inputBox")
        self.verticalLayout.addWidget(self.inputBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.app_logo = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.app_logo.setFont(font)
        self.app_logo.setStyleSheet(
            "QLabel{\n"
            "font-size: 72px;\n"
            "color: rgb(255, 203, 99);\n"
            "background-color: white;\n"
            "border-color: black;\n"
            "border-radius: 10px;\n"
            "border-style: none;\n"
            "padding-top: 10px;\n"
            "padding-bottom: 10px;\n"
            "margin-top: 10px;\n"
            "margin-bottom: 10px;\n"
            "margin-left: 0px;\n"
            "margin-right: 0px;\n"
            "}"
        )
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.verticalLayout_3.addWidget(self.app_logo)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(
            self.groupBox, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter
        )
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_button.setText(_translate("MainWindow", "Login"))
        self.new_label.setText(_translate("MainWindow", "Is it your first time here?"))
        self.new_button.setText(_translate("MainWindow", "Make a new account"))
        self.email_label.setText(_translate("MainWindow", "Email:"))
        self.pw_label.setText(_translate("MainWindow", "Password:"))
        self.app_logo.setText(_translate("MainWindow", "GoldApp"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
