# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contactpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(875, 838)
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
        self.app_logo.setMaximumSize(QtCore.QSize(645, 200))
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
        self.page_content.setMinimumSize(QtCore.QSize(0, 600))
        self.page_content.setObjectName("page_content")
        self.gridLayout = QtWidgets.QGridLayout(self.page_content)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.heading = QtWidgets.QLabel(self.page_content)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setStyleSheet("font-size: 32px;")
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout_2.addWidget(self.heading)
        self.widget = QtWidgets.QWidget(self.page_content)
        self.widget.setMinimumSize(QtCore.QSize(0, 270))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setObjectName("widget1")
        self.medical_box = QtWidgets.QHBoxLayout(self.widget1)
        self.medical_box.setContentsMargins(-1, 1, -1, -1)
        self.medical_box.setObjectName("medical_box")
        self.name = QtWidgets.QLabel(self.widget1)
        self.name.setStyleSheet("font-size: 24px;\n"
"margin-left: 10px;")
        self.name.setObjectName("name")
        self.medical_box.addWidget(self.name)
        self.number = QtWidgets.QLabel(self.widget1)
        self.number.setStyleSheet("font-size: 20px;")
        self.number.setObjectName("number")
        self.medical_box.addWidget(self.number)
        self.verticalLayout.addWidget(self.widget1)
        self.widget2 = QtWidgets.QWidget(self.widget)
        self.widget2.setObjectName("widget2")
        self.scam_box = QtWidgets.QHBoxLayout(self.widget2)
        self.scam_box.setObjectName("scam_box")
        self.name2 = QtWidgets.QLabel(self.widget2)
        self.name2.setStyleSheet("font-size: 24px;\n"
"margin-left: 10px;")
        self.name2.setObjectName("name2")
        self.scam_box.addWidget(self.name2)
        self.phone2 = QtWidgets.QLabel(self.widget2)
        self.phone2.setStyleSheet("font-size: 20px;")
        self.phone2.setObjectName("phone2")
        self.scam_box.addWidget(self.phone2)
        self.verticalLayout.addWidget(self.widget2)
        self.widget3 = QtWidgets.QWidget(self.widget)
        self.widget3.setObjectName("widget3")
        self.general_box = QtWidgets.QHBoxLayout(self.widget3)
        self.general_box.setObjectName("general_box")
        self.name3 = QtWidgets.QLabel(self.widget3)
        self.name3.setStyleSheet("font-size: 24px;\n"
"margin-left: 10px;")
        self.name3.setObjectName("name3")
        self.general_box.addWidget(self.name3)
        self.phone3 = QtWidgets.QLabel(self.widget3)
        self.phone3.setStyleSheet("font-size: 20px;")
        self.phone3.setObjectName("phone3")
        self.general_box.addWidget(self.phone3)
        self.verticalLayout.addWidget(self.widget3)
        self.verticalLayout_2.addWidget(self.widget)
        self.photo = QtWidgets.QLabel(self.page_content)
        self.photo.setMaximumSize(QtCore.QSize(411, 221))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../image/callcenter.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignCenter)
        self.photo.setObjectName("photo")
        self.verticalLayout_2.addWidget(self.photo, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.page_content, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.app_logo.setText(_translate("Form", "GoldApp"))
        self.heading.setText(_translate("Form", "Contact details: {location}"))
        self.name.setText(_translate("Form", "Medical Assistance"))
        self.number.setText(_translate("Form", "Call {number}"))
        self.name2.setText(_translate("Form", "Victim of senior scam?"))
        self.phone2.setText(_translate("Form", "Call {number}"))
        self.name3.setText(_translate("Form", "General assistance"))
        self.phone3.setText(_translate("Form", "Call {number}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
