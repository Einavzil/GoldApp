# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dzenis Madzovic\OneDrive - Högskolan Kristianstad\Skrivbordet\Projects\GoldApp\src\MentalPage\mental_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(658, 756)
        Form.setStyleSheet("background-color: rgb(220, 221, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.logo_layout = QtWidgets.QHBoxLayout()
        self.logo_layout.setObjectName("logo_layout")
        self.app_logo = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.app_logo.setFont(font)
        self.app_logo.setStyleSheet("QLabel{\n"
"color: rgb(255, 203, 99);\n"
"background-color: white;\n"
"border-color: black;\n"
"border-radius: 10px;\n"
"border-style: none;\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"margin-left: 0px;\n"
"margin-right: 0px;\n"
"}")
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.logo_layout.addWidget(self.app_logo)
        self.gridLayout_2.addLayout(self.logo_layout, 0, 0, 1, 1)
        self.page_content = QtWidgets.QWidget(self.frame)
        self.page_content.setObjectName("page_content")
        self.gridLayout = QtWidgets.QGridLayout(self.page_content)
        self.gridLayout.setObjectName("gridLayout")
        self.headers_layout = QtWidgets.QWidget(self.page_content)
        self.headers_layout.setMinimumSize(QtCore.QSize(604, 220))
        self.headers_layout.setObjectName("headers_layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.headers_layout)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QLabel(self.headers_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.header.setFont(font)
        self.header.setStyleSheet("font: 63 23pt \"Segoe UI Semibold\";\n"
"")
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setObjectName("header")
        self.verticalLayout.addWidget(self.header)
        self.subheader = QtWidgets.QTextBrowser(self.headers_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subheader.sizePolicy().hasHeightForWidth())
        self.subheader.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.subheader.setFont(font)
        self.subheader.setStyleSheet("margin-top: 5px;\n"
"margin-left: 7px;\n"
"margin-right: 7px;\n"
"")
        self.subheader.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.subheader.setFrameShadow(QtWidgets.QFrame.Plain)
        self.subheader.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.subheader.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.subheader.setObjectName("subheader")
        self.verticalLayout.addWidget(self.subheader)
        self.gridLayout.addWidget(self.headers_layout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.page_content)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.help_page_button = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.help_page_button.setFont(font)
        self.help_page_button.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 18px;\n"
"margin-left: 10px;\n"
"margin-right: 10px;\n"
"margin-bottom: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(255, 220, 99);\n"
"}")
        self.help_page_button.setObjectName("help_page_button")
        self.verticalLayout_2.addWidget(self.help_page_button)
        self.photo = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo.sizePolicy().hasHeightForWidth())
        self.photo.setSizePolicy(sizePolicy)
        self.photo.setMinimumSize(QtCore.QSize(109, 100))
        self.photo.setMaximumSize(QtCore.QSize(309, 300))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setStyleSheet("display: inline-block;\n"
"min-width: 100px;\n"
"min-height: 100px;\n"
"max-width: 300px;\n"
"max-height: 300px;\n"
"margin-left:9px;\n"
"border-radius: 3px;\n"
"")
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("c:\\Users\\Dzenis Madzovic\\OneDrive - Högskolan Kristianstad\\Skrivbordet\\Projects\\GoldApp\\src\\MentalPage\\../image/1111.png"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.verticalLayout_2.addWidget(self.photo, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.page_content, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.app_logo.setText(_translate("Form", "GoldApp"))
        self.header.setText(_translate("Form", "We are here for you"))
        self.subheader.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:16px; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:400;\">According to your last daily surveys, it seems like you are below average in your mental state.<br />Please, do not hesitate to seek mental help from professionals or through our help page.</span></p></body></html>"))
        self.help_page_button.setText(_translate("Form", "Go to help page"))
