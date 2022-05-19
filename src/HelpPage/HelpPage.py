# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelpPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os

path = os.path.dirname(os.path.abspath(f"{__file__}\.."))
import help_page_conn
from ContactPage.ContactPage import ContactPage


class HelpPage(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self._heightMask = self.height()
        self.animation = QPropertyAnimation(self, b"height")
        self.animation.setDuration(1000)
        self.animation.setStartValue(self.height())
        self.animation.setEndValue(-1)
        self.animation.finished.connect(self.close)
        self.isStarted = False

    def heightMask(self):
        return self._heightMask

    def heightPercentage(self, value):
        self._heightMask = value
        rect = QRect(0, 0, self.width(), self.height())
        self.setMask(QRegion(rect))

    def closeEvent(self, event):
        if not self.isStarted:
            self.animation.start()
            self.isStarted = True
            event.ignore()
        else:
            QWidget.closeEvent(self, event)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setStyleSheet("background-color: rgb(220, 221, 255);")
        MainWindow.showMaximized()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1173, 725))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.submit_button = QPushButton(
            self.scrollAreaWidgetContents,
            clicked=lambda: self.collect_form_details(MainWindow),
        )
        self.submit_button.setStyleSheet(
            "QPushButton{\n"
            "color: white;\n"
            "font-size: 15px;\n"
            "font-family: Segoe UI Symbol;\n"
            "background-color: rgb(255, 203, 99);\n"
            "border-width: 0px;\n"
            "border-radius:75px;\n"
            "min-height: 150px;\n"
            "min-width: 150px;\n"
            "max-height: 150px;\n"
            "max-width: 150px;\n"
            "margin-top: 50px;"
            "}"
            "QPushButton:Hover{\n"
            "background-color: rgb(255, 220, 99);\n"
            "}"
        )
        self.submit_button.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.submit_button, 4, 1, 1, 1, Qt.AlignHCenter)
        spacerItem = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 313, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 2, 1, 1, 1)
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget1 = QWidget(self.widget)
        self.widget1.setMinimumSize(QSize(520, 0))
        self.widget1.setStyleSheet(
            "background-color: white;\n" "border-radius: 5px;\n" "padding-left: 50px;\n"
        )
        self.widget1.setObjectName("widget1")
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setMinimumSize(QSize(600, 0))
        font = QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(
            "font-size: 20px;\n"
            "color: white;\n"
            "padding: 5px;\n"
            "background-color: orange;\n"
            "text-align: center;"
        )
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignVCenter)
        self.widget_3 = QWidget(self.widget1)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget2 = QWidget(self.widget1)
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QVBoxLayout(self.widget2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_2 = QLineEdit(self.widget2)
        self.lineEdit_2.setStyleSheet("font-size: 20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_4 = QLineEdit(self.widget2)
        self.lineEdit_4.setStyleSheet("font-size: 20px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_3 = QLineEdit(self.widget2)
        self.lineEdit_3.setStyleSheet("font-size: 20px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_5 = QLineEdit(self.widget2)
        self.lineEdit_5.setStyleSheet("font-size: 20px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.widget_4 = QWidget(self.widget2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.verticalLayout_2.addWidget(self.widget2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.widget3 = QWidget(self.widget1)
        self.widget3.setObjectName("widget3")
        self.gridLayout.addWidget(self.widget3, 0, 0, 1, 1)
        self.widget_2 = QWidget(self.widget1)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.widget1)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setStyleSheet("margin-left: 15px")
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.widget_6)
        spacerItem3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.press_here_button = QPushButton(
            self.widget, clicked=lambda: self.open_contact_page()
        )
        self.press_here_button.setStyleSheet(
            "QPushButton{\n"
            "font-size: 15px;\n"
            "font-family: Segoe UI Symbol;\n"
            "color: white;\n"
            "background-color: rgb(255, 203, 99);\n"
            "border-width: 0px;\n"
            "border-radius:75px;\n"
            "min-height: 150px;\n"
            "min-width: 150px;\n"
            "max-height: 150px;\n"
            "max-width: 150px;\n"
            "}"
            "QPushButton:Hover{\n"
            "background-color: rgb(255, 220, 99);\n"
            "}"
        )
        self.press_here_button.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.press_here_button)
        self.gridLayout_3.addWidget(self.widget, 0, 1, 2, 1)
        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setStyleSheet(
            " background-color: rgb(234, 234, 255);\n" "border-radius: 3px;\n "
        )
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_4 = QGridLayout(self.widget_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.labels_layout = QWidget(self.widget_7)
        self.labels_layout.setStyleSheet(
            "margin-left: 7px;\n" "font-size: 25px;\n" "border-color: black;"
        )
        self.labels_layout.setObjectName("labels_layout")
        self.labels = QVBoxLayout(self.labels_layout)
        self.labels.setObjectName("labels")
        self.email_label = QLabel(self.labels_layout)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.email_label.setFont(font)
        self.email_label.setStyleSheet("margin-right: 130px;")
        self.email_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.email_label.setObjectName("email_label")
        self.labels.addWidget(self.email_label)
        self.first_label = QLabel(self.labels_layout)
        font = QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        self.first_label.setFont(font)
        self.first_label.setStyleSheet("margin-right: 74px;")
        self.first_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.first_label.setObjectName("first_label")
        self.labels.addWidget(self.first_label)
        self.last_label = QLabel(self.labels_layout)
        self.last_label.setFont(font)
        self.last_label.setStyleSheet("margin-right: 76px;")
        self.last_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.last_label.setObjectName("last_label")
        self.labels.addWidget(self.last_label)
        self.phone_label = QLabel(self.labels_layout)
        self.phone_label.setFont(font)
        self.phone_label.setStyleSheet("margin-right: 26px;")
        self.phone_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.phone_label.setObjectName("phone_label")
        self.labels.addWidget(self.phone_label)
        self.issue_type_label = QLabel(self.labels_layout)
        self.issue_type_label.setFont(font)
        self.issue_type_label.setStyleSheet("margin-right: 120px;")
        self.issue_type_label.setObjectName("passwor_label")
        self.labels.addWidget(self.issue_type_label)

        self.issue_desc_label = QLabel(self.labels_layout)
        self.issue_desc_label.setFont(font)
        self.issue_desc_label.setStyleSheet("margin-right: 120px;")
        self.issue_desc_label.setObjectName("passwor_label_3")
        self.labels.addWidget(self.issue_desc_label)

        self.location_label = QLabel(self.labels_layout)
        self.location_label.setFont(font)
        self.location_label.setStyleSheet("margin-bottom: 0px;")
        self.location_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )
        self.location_label.setObjectName("rep_pass_label")
        self.labels.addWidget(self.location_label)
        self.location_label = QLabel(self.labels_layout)
        self.location_label.setFont(font)
        self.location_label.setStyleSheet("margin-right: 90px;")
        self.location_label.setObjectName("passwor_label_2")
        self.labels.addWidget(self.location_label)
        self.gridLayout_4.addWidget(self.labels_layout, 0, 0, 1, 1)
        self.inputs_layout = QWidget(self.widget_7)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inputs_layout.sizePolicy().hasHeightForWidth()
        )
        self.inputs_layout.setSizePolicy(sizePolicy)
        self.inputs_layout.setStyleSheet("margin-top: 8px;\n" "margin-right: 7px;")
        self.inputs_layout.setObjectName("inputs_layout")
        self.inputs = QVBoxLayout(self.inputs_layout)
        self.inputs.setObjectName("inputs")
        self.email_input = QLineEdit(self.inputs_layout)
        self.email_input.setFont(font)
        self.email_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: grey;"
        )
        self.email_input.setText(f"{help_page_conn.user_email()}")
        self.email_input.setObjectName("email_input")
        self.email_input.setReadOnly(True)
        self.inputs.addWidget(self.email_input)
        self.first_input = QLineEdit(self.inputs_layout)
        self.first_input.setFont(font)
        self.first_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: grey;"
        )
        self.first_input.setText(f"{help_page_conn.user_first_name()}")
        self.first_input.setObjectName("first_input")
        self.first_input.setReadOnly(True)
        self.inputs.addWidget(self.first_input)
        self.last_input = QLineEdit(self.inputs_layout)
        self.last_input.setFont(font)
        self.last_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: grey;"
        )
        self.last_input.setText(f"{help_page_conn.user_last_name()}")
        self.last_input.setObjectName("last_input")
        self.last_input.setReadOnly(True)
        self.inputs.addWidget(self.last_input)
        self.phone_input = QLineEdit(self.inputs_layout)
        self.phone_input.setFont(font)
        self.phone_input.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "color: grey;"
        )
        self.phone_input.setText(f"{help_page_conn.user_phone()}")
        self.phone_input.setObjectName("phone_input")
        self.phone_input.setReadOnly(True)
        self.inputs.addWidget(self.phone_input)
        self.issue_type_comboBox = QComboBox(self.inputs_layout)
        self.issue_type_comboBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.issue_type_comboBox.sizePolicy().hasHeightForWidth()
        )
        self.issue_type_comboBox.setSizePolicy(sizePolicy)
        self.issue_type_comboBox.setMinimumSize(QSize(0, 0))
        self.issue_type_comboBox.setFont(font)
        self.issue_type_comboBox.setStyleSheet("background-color:  rgb(255, 255, 255);")
        self.issue_type_comboBox.setObjectName("pass_input")
        self.issue_type_comboBox.setFrame(True)
        self.inputs.addWidget(self.issue_type_comboBox)
        self.textEdit = QTextEdit(self.inputs_layout)
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("background-color: white;\n" "font-size: 17px;")
        self.inputs.addWidget(self.textEdit)
        self.location_comboBox = QComboBox(self.inputs_layout)
        self.location_comboBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.location_comboBox.sizePolicy().hasHeightForWidth()
        )
        self.location_comboBox.setSizePolicy(sizePolicy)
        self.location_comboBox.setMinimumSize(QSize(0, 0))

        self.location_comboBox.setFont(font)
        self.location_comboBox.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "padding-left: 0px;"
        )
        self.location_comboBox.setFrame(True)
        self.location_comboBox.setObjectName("comboBox")
        self.location_comboBox.addItem("")
        # self.comboBox.addItem("")
        self.inputs.addWidget(self.location_comboBox)
        self.gridLayout_4.addWidget(self.inputs_layout, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.widget_7, 3, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1200, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.lineEdit.setText(
            _translate("MainWindow", "Want to talk with professionals?")
        )
        self.lineEdit_2.setText(
            _translate("MainWindow", "The button to the right will")
        )
        self.lineEdit_4.setText(
            _translate("MainWindow", "bring up call centers local to your area.")
        )
        self.lineEdit_3.setText(
            _translate("MainWindow", "If you want more personilized help")
        )
        self.lineEdit_5.setText(
            _translate("MainWindow", "please fill up the form below.")
        )
        self.press_here_button.setText(_translate("MainWindow", "Press Here"))
        self.email_label.setText(_translate("MainWindow", "Email:"))
        self.first_label.setText(_translate("MainWindow", "First name:"))
        self.last_label.setText(_translate("MainWindow", "Last name:"))
        self.phone_label.setText(_translate("MainWindow", "Phone number:"))
        self.issue_type_label.setText(_translate("MainWindow", "Issue type: "))
        issue_list = [
            "Choose..",
            "Health",
            "Transportation",
            "Mental Health",
            "Bored",
            "Other",
        ]
        self.issue_type_comboBox.addItems(issue_list)
        self.issue_desc_label.setText(_translate("MainWindow", "Issue description: "))
        self.location_label.setText(_translate("MainWindow", "Location:"))
        self.location_comboBox.setItemText(
            0, _translate("MainWindow", f"{help_page_conn.user_location()}")
        )
        # self.comboBox.setItemText(1, _translate("MainWindow", "Stockholm"))

    def show_popup_submitted(self):
        msg = QMessageBox()
        msg.setWindowTitle("sumbitted succesfully")
        msg.setText(
            "Your form submitted succesfully. We will try to contact you back as soon as possible."
        )
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def open_contact_page(self):
        self.window = QWidget()
        self.ui = ContactPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def collect_form_details(self, MainWindow):
        max_chars_desc = 300
        email = help_page_conn.user_email()
        if self.issue_type_comboBox.currentIndex() == 0:
            self.show_popup_choose_type()
            return False
        issue_type = self.issue_type_comboBox.currentText()
        if len(self.textEdit.toPlainText()) > max_chars_desc:
            self.show_popup_too_long()
            return False
        issue_description = self.textEdit.toPlainText()
        row_count = help_page_conn.insert_form(email, issue_type, issue_description)
        if row_count == 1:
            self.show_popup_submitted()
            MainWindow.close()

    def show_popup_choose_type(self):
        msg = QMessageBox()
        msg.setWindowTitle("issue type not chosen")
        msg.setText("An issue type was not selected. Please select and try again")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def show_popup_too_long(self):
        msg = QMessageBox()
        msg.setWindowTitle("issue desc is too long")
        msg.setText("Issue description is too long. Try again")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelpPage()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
