# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/NewAccount/NewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

sys.path.insert(0, "../src")
import signup


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()

    def passwords_match(self):
        if self.pass_input.text() != self.rep_pass_input.text():
            return False
        elif self.pass_input.text() == "":
            return False
        return True

    def create_account(self, Form):

        while "@" not in self.email_input.text():
            self.show_popup_email()
            return False

        while self.first_input.text() == "":
            self.show_popup_fname()
            return False

        while not self.passwords_match():
            self.show_popup_pass()
            return False

        email = signup.insert_account(
            self.first_input.text(),
            self.last_input.text(),
            self.email_input.text(),
            self.pass_input.text(),
            self.phone_input.text(),
            self.comboBox.currentText(),
        )

        self.input_interest(email)
        Form.close()

    def input_interest(self, email):
        if self.checkBox_1.isChecked():
            signup.add_interest(email, 1)
        if self.checkBox_2.isChecked():
            signup.add_interest(email, 2)
        if self.checkBox_3.isChecked():
            signup.add_interest(email, 3)
        if self.checkBox_4.isChecked():
            signup.add_interest(email, 4)
        if self.checkBox_5.isChecked():
            signup.add_interest(email, 5)
        if self.checkBox_6.isChecked():
            signup.add_interest(email, 6)
        if self.checkBox_7.isChecked():
            signup.add_interest(email, 7)
        if self.checkBox_8.isChecked():
            signup.add_interest(email, 8)
        if self.checkBox_9.isChecked():
            signup.add_interest(email, 9)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(662, 812)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(1800, 1200))
        Form.setMinimumSize(QtCore.QSize(1200, 600))
        Form.setStyleSheet("background-color: rgb(220, 221, 255);")
        Form.showFullScreen()
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 662, 812))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.interests_layout = QtWidgets.QGroupBox(self.groupBox)
        self.interests_layout.setObjectName("interests_layout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.interests_layout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget1 = QtWidgets.QWidget(self.interests_layout)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.interests_lable = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.interests_lable.setFont(font)
        self.interests_lable.setStyleSheet("margin-bottom: 10px;\n" "margin-top: 10px;")
        self.interests_lable.setObjectName("interests_lable")
        self.verticalLayout.addWidget(self.interests_lable)
        self.widget2 = QtWidgets.QWidget(self.widget1)
        self.widget2.setObjectName("widget2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout.setObjectName("gridLayout")

        # Checkbox 1
        self.checkBox_1 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox_1, 0, 0, 1, 1)
        # Checkbox 2
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        # Checkbox 3
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        # Checkbox 4
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 0, 1, 1, 1)
        # Checkbox 5
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        # Checkbox 6
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 2, 1, 1, 1)
        # Checkbox 7
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 0, 2, 1, 1)
        # Checkbox 8
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 1, 2, 1, 1)
        # Checkbox 9
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(14)
        self.checkBox_9.setFont(font)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 2, 1, 1)

        self.verticalLayout.addWidget(self.widget2)
        self.horizontalLayout.addWidget(self.widget1)
        self.gridLayout_5.addWidget(self.interests_layout, 2, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.app_logo = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.app_logo.setFont(font)
        self.app_logo.setStyleSheet(
            "QLabel{\n"
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
            "}"
        )
        self.app_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.app_logo.setObjectName("app_logo")
        self.horizontalLayout_5.addWidget(self.app_logo)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labels_layout = QtWidgets.QWidget(self.groupBox)
        self.labels_layout.setStyleSheet("margin-left: 7px;")
        self.labels_layout.setObjectName("labels_layout")
        self.labels = QtWidgets.QVBoxLayout(self.labels_layout)
        self.labels.setObjectName("labels")
        self.email_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("margin-right: 130px;")
        self.email_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.email_label.setObjectName("email_label")
        self.labels.addWidget(self.email_label)
        self.first_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.first_label.setFont(font)
        self.first_label.setStyleSheet("margin-right: 74px;")
        self.first_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.first_label.setObjectName("first_label")
        self.labels.addWidget(self.first_label)
        self.last_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.last_label.setFont(font)
        self.last_label.setStyleSheet("margin-right: 76px;")
        self.last_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.last_label.setObjectName("last_label")
        self.labels.addWidget(self.last_label)
        self.phone_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("margin-right: 26px;")
        self.phone_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.phone_label.setObjectName("phone_label")
        self.labels.addWidget(self.phone_label, 0, QtCore.Qt.AlignLeft)
        self.passwor_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.passwor_label.setFont(font)
        self.passwor_label.setStyleSheet("margin-right: 120px;")
        self.passwor_label.setObjectName("passwor_label")
        self.labels.addWidget(self.passwor_label)
        self.rep_pass_label = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.rep_pass_label.setFont(font)
        self.rep_pass_label.setStyleSheet("margin-right: 35px;")
        self.rep_pass_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.rep_pass_label.setObjectName("rep_pass_label")
        self.labels.addWidget(self.rep_pass_label)
        self.passwor_label_2 = QtWidgets.QLabel(self.labels_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.passwor_label_2.setFont(font)
        self.passwor_label_2.setStyleSheet("margin-right: 90px;")
        self.passwor_label_2.setObjectName("passwor_label_2")
        self.labels.addWidget(self.passwor_label_2)
        self.gridLayout_2.addWidget(self.labels_layout, 0, 0, 1, 1)
        self.inputs_layout = QtWidgets.QWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inputs_layout.sizePolicy().hasHeightForWidth()
        )
        self.inputs_layout.setSizePolicy(sizePolicy)
        self.inputs_layout.setStyleSheet("margin-top: 4px;\n" "margin-right: 7px;")
        self.inputs_layout.setObjectName("inputs_layout")
        self.inputs = QtWidgets.QVBoxLayout(self.inputs_layout)
        self.inputs.setObjectName("inputs")
        self.email_input = QtWidgets.QLineEdit(self.inputs_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.email_input.setFont(font)
        self.email_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.inputs.addWidget(self.email_input)
        self.first_input = QtWidgets.QLineEdit(self.inputs_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.first_input.setFont(font)
        self.first_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.first_input.setObjectName("first_input")
        self.inputs.addWidget(self.first_input)
        self.last_input = QtWidgets.QLineEdit(self.inputs_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.last_input.setFont(font)
        self.last_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.last_input.setObjectName("last_input")
        self.inputs.addWidget(self.last_input)
        self.phone_input = QtWidgets.QLineEdit(self.inputs_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.phone_input.setFont(font)
        self.phone_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.phone_input.setText("")
        self.phone_input.setObjectName("phone_input")
        self.inputs.addWidget(self.phone_input)
        self.pass_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pass_input.setFont(font)
        self.pass_input.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.pass_input.setObjectName("pass_input")
        self.inputs.addWidget(self.pass_input)
        self.rep_pass_input = QtWidgets.QLineEdit(self.inputs_layout)
        self.rep_pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(16)
        self.rep_pass_input.setFont(font)
        self.rep_pass_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rep_pass_input.setText("")
        self.rep_pass_input.setObjectName("rep_pass_input")
        self.inputs.addWidget(self.rep_pass_input)
        self.comboBox = QtWidgets.QComboBox(self.inputs_layout)
        self.comboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "padding-left: 0px;"
        )
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.inputs.addWidget(self.comboBox)
        self.gridLayout_2.addWidget(self.inputs_layout, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.create_layout = QtWidgets.QVBoxLayout()
        self.create_layout.setObjectName("create_layout")
        spacerItem = QtWidgets.QSpacerItem(
            20,
            20,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        self.create_layout.addItem(spacerItem)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Create account button
        self.create_button = QtWidgets.QPushButton(
            self.groupBox, clicked=lambda: self.create_account(Form)
        )
        sizePolicy.setHeightForWidth(
            self.create_button.sizePolicy().hasHeightForWidth()
        )
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.create_button.setFont(font)
        self.create_button.setSizePolicy(sizePolicy)
        self.create_button.setStyleSheet(
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
        self.create_button.setObjectName("create_button")
        self.create_layout.addWidget(self.create_button)
        self.gridLayout_5.addLayout(self.create_layout, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.interests_lable.setText(_translate("Form", "Choose your interests:"))
        self.checkBox_4.setText(_translate("Form", "Chess"))
        self.checkBox_6.setText(_translate("Form", "Music"))
        self.checkBox_3.setText(_translate("Form", "Cinema/Theater"))
        self.checkBox_2.setText(_translate("Form", "Cooking"))
        self.checkBox_8.setText(_translate("Form", "Hunting"))
        self.checkBox_1.setText(_translate("Form", "Fishing"))
        self.checkBox_5.setText(_translate("Form", "Art"))
        self.checkBox_7.setText(_translate("Form", "Baking"))
        self.checkBox_9.setText(_translate("Form", "Taking walks"))
        self.app_logo.setText(_translate("Form", "GoldApp"))
        self.email_label.setText(_translate("Form", "Email:"))
        self.first_label.setText(_translate("Form", "First name:"))
        self.last_label.setText(_translate("Form", "Last name:"))
        self.phone_label.setText(_translate("Form", "Phone number:"))
        self.passwor_label.setText(_translate("Form", "Password:"))
        self.rep_pass_label.setText(_translate("Form", "Repeat password:"))
        self.passwor_label_2.setText(_translate("Form", "Location:"))
        self.comboBox.setItemText(0, _translate("Form", "Skåne"))
        self.comboBox.setItemText(1, _translate("Form", "Stockholm"))
        self.create_button.setText(_translate("Form", "Create"))

    def show_popup_pass(self):
        msg = QMessageBox()
        msg.setWindowTitle("passwords not match")
        msg.setText("Error")
        msg.setInformativeText(
            "Either your passwords don't match or you didn't enter a password."
        )
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def show_popup_email(self):
        msg = QMessageBox()
        msg.setWindowTitle("email invalid")
        msg.setText("Enter a valid email adress.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def show_popup_fname(self):
        msg = QMessageBox()
        msg.setWindowTitle("name is null")
        msg.setText("You have to enter a name.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
