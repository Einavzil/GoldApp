# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Dzenis Madzovic\OneDrive - Högskolan Kristianstad\Skrivbordet\Projects\GoldApp\src\examples\meetings_events_single.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(789, 697)
        Form.setStyleSheet("background-color: rgb(220, 221, 255);")
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
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
        self.horizontalLayout_5.addWidget(self.app_logo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setEnabled(True)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 9, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.events_loc_label = QtWidgets.QLabel(self.widget_2)
        self.events_loc_label.setMinimumSize(QtCore.QSize(404, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.events_loc_label.setFont(font)
        self.events_loc_label.setStyleSheet("<html><head/><body><p align=\"center\">Local Events and Meetups<span id=\"location\">:</span></p></body></html> ")
        self.events_loc_label.setScaledContents(False)
        self.events_loc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.events_loc_label.setObjectName("events_loc_label")
        self.horizontalLayout.addWidget(self.events_loc_label)
        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setStyleSheet("margin-bottom: 8px;\n"
"background: white;\n"
"border-radius: 5px;\n"
"")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font-size: 18px;\n"
"padding: 5px;\n"
"margin-left:5px;")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("font-size: 13px;\n"
"padding: 5px;\n"
"margin-left:5px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("font-size: 13px;\n"
"padding: 5px;\n"
"margin-left:5px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("font-size: 13px;\n"
"padding: 5px;\n"
"margin-left:5px;\n"
"margin-bottom:5px;\n"
"border-radious: 10px;\n"
"min-height: 50px;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addWidget(self.widget, 3, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setStyleSheet("padding-left: 8px;\n"
"padding-bottom: 5px;\n"
"max-height: 500px;\n"
"background:white;\n"
"border-radius: 5px;")
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.photo = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.photo.setFont(font)
        self.photo.setStyleSheet("display: inline-block;\n"
"margin bottom: 3px;\n"
"min-height: 100px;\n"
"max-height: 200px;\n"
"border-radius: 3px;\n"
"")
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("c:\\Users\\Dzenis Madzovic\\OneDrive - Högskolan Kristianstad\\Skrivbordet\\Projects\\GoldApp\\src\\examples\\../../../../../Downloads/vlad-sargu-ItphH2lGzuI-unsplash.jpg"))
        self.photo.setScaledContents(False)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.horizontalLayout_2.addWidget(self.photo)
        self.gridLayout_3.addWidget(self.widget1, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:  rgb(255, 203, 99);\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: white;\n"
"padding: 10px 23px;\n"
"margin: 10px 60px 10px 60px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 13px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  rgb(255, 220, 99);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_4.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.app_logo.setText(_translate("Form", "GoldApp"))
        self.events_loc_label.setText(_translate("Form", "<html><head/><body><p align=\"center\">Local Events and Meetups<span id=\"location\">:</span></p></body></html> "))
        self.label.setText(_translate("Form", "Event: "))
        self.label_2.setText(_translate("Form", "Date & Time: "))
        self.label_3.setText(_translate("Form", "Location: "))
        self.label_4.setText(_translate("Form", "Description:"))
        self.pushButton.setText(_translate("Form", "Back"))
