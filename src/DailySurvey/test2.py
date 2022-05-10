# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DailySurvey.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 1000)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(950, 950))
        Form.setStyleSheet("background-color: rgb(220, 221, 255);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_layout = QtWidgets.QWidget(Form)
        self.main_layout.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_layout.sizePolicy().hasHeightForWidth())
        self.main_layout.setSizePolicy(sizePolicy)
        self.main_layout.setMinimumSize(QtCore.QSize(900, 900))
        self.main_layout.setMaximumSize(QtCore.QSize(950, 900))
        self.main_layout.setObjectName("main_layout")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.main_layout)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.bottom_layout = QtWidgets.QVBoxLayout()
        self.bottom_layout.setContentsMargins(-1, 10, -1, -1)
        self.bottom_layout.setObjectName("bottom_layout")
        self.top_text = QtWidgets.QWidget(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_text.sizePolicy().hasHeightForWidth())
        self.top_text.setSizePolicy(sizePolicy)
        self.top_text.setMinimumSize(QtCore.QSize(896, 80))
        self.top_text.setMaximumSize(QtCore.QSize(896, 80))
        self.top_text.setObjectName("top_text")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.top_text)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 1)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.text1 = QtWidgets.QLabel(self.top_text)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text1.sizePolicy().hasHeightForWidth())
        self.text1.setSizePolicy(sizePolicy)
        self.text1.setMinimumSize(QtCore.QSize(892, 37))
        self.text1.setMaximumSize(QtCore.QSize(892, 37))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.text1.setFont(font)
        self.text1.setStyleSheet("")
        self.text1.setAlignment(QtCore.Qt.AlignCenter)
        self.text1.setObjectName("text1")
        self.gridLayout_4.addWidget(self.text1, 0, 0, 1, 1)
        self.text2 = QtWidgets.QLabel(self.top_text)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text2.sizePolicy().hasHeightForWidth())
        self.text2.setSizePolicy(sizePolicy)
        self.text2.setMinimumSize(QtCore.QSize(892, 31))
        self.text2.setMaximumSize(QtCore.QSize(892, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.text2.setFont(font)
        self.text2.setStyleSheet("")
        self.text2.setAlignment(QtCore.Qt.AlignCenter)
        self.text2.setObjectName("text2")
        self.gridLayout_4.addWidget(self.text2, 1, 0, 1, 1)
        self.bottom_layout.addWidget(self.top_text)
        self.questions_layout = QtWidgets.QWidget(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.questions_layout.sizePolicy().hasHeightForWidth()
        )
        self.questions_layout.setSizePolicy(sizePolicy)
        self.questions_layout.setMinimumSize(QtCore.QSize(700, 498))
        self.questions_layout.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.questions_layout.setObjectName("questions_layout")
        self.gridLayout = QtWidgets.QGridLayout(self.questions_layout)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.question1_layout = QtWidgets.QVBoxLayout()
        self.question1_layout.setContentsMargins(-1, 5, -1, 1)
        self.question1_layout.setObjectName("question1_layout")
        self.question1_text = QtWidgets.QLabel(self.questions_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.question1_text.setFont(font)
        self.question1_text.setStyleSheet("")
        self.question1_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question1_text.setObjectName("question1_text")
        self.question1_layout.addWidget(self.question1_text)
        self.groupbox = QtWidgets.QGroupBox(self.questions_layout)
        self.groupbox.setObjectName("groupbox")
        self.question1_answers = QtWidgets.QHBoxLayout(self.groupbox)
        self.question1_answers.setContentsMargins(-1, 10, -1, 10)
        self.question1_answers.setObjectName("question1_answers")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.question1_answers.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.question1_answers.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.question1_answers.addWidget(self.radioButton)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.question1_answers.addWidget(self.radioButton_5)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupbox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.question1_answers.addWidget(self.radioButton_2)
        self.question1_layout.addWidget(self.groupbox)
        self.gridLayout.addLayout(self.question1_layout, 0, 0, 1, 1)
        self.question2_layout = QtWidgets.QVBoxLayout()
        self.question2_layout.setContentsMargins(-1, 10, -1, 1)
        self.question2_layout.setObjectName("question2_layout")
        self.question2_text = QtWidgets.QLabel(self.questions_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.question2_text.setFont(font)
        self.question2_text.setStyleSheet("")
        self.question2_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question2_text.setObjectName("question2_text")
        self.question2_layout.addWidget(self.question2_text)
        self.question2_answers_2 = QtWidgets.QGroupBox(self.questions_layout)
        self.question2_answers_2.setObjectName("question2_answers_2")
        self.question2_answers = QtWidgets.QHBoxLayout(self.question2_answers_2)
        self.question2_answers.setContentsMargins(-1, 10, -1, 10)
        self.question2_answers.setObjectName("question2_answers")
        self.radioButton_6 = QtWidgets.QRadioButton(self.question2_answers_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.question2_answers.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.question2_answers_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.question2_answers.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.question2_answers_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.question2_answers.addWidget(self.radioButton_8)
        self.radioButton_9 = QtWidgets.QRadioButton(self.question2_answers_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setObjectName("radioButton_9")
        self.question2_answers.addWidget(self.radioButton_9)
        self.radioButton_10 = QtWidgets.QRadioButton(self.question2_answers_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setObjectName("radioButton_10")
        self.question2_answers.addWidget(self.radioButton_10)
        self.question2_layout.addWidget(self.question2_answers_2)
        self.gridLayout.addLayout(self.question2_layout, 1, 0, 1, 1)
        self.question3_layout = QtWidgets.QVBoxLayout()
        self.question3_layout.setContentsMargins(-1, 10, -1, 1)
        self.question3_layout.setObjectName("question3_layout")
        self.question3_text = QtWidgets.QLabel(self.questions_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.question3_text.setFont(font)
        self.question3_text.setStyleSheet("")
        self.question3_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question3_text.setObjectName("question3_text")
        self.question3_layout.addWidget(self.question3_text)
        self.groupbox1 = QtWidgets.QGroupBox(self.questions_layout)
        self.groupbox1.setObjectName("groupbox1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupbox1)
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_11 = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_11.setFont(font)
        self.radioButton_11.setObjectName("radioButton_11")
        self.horizontalLayout_2.addWidget(self.radioButton_11)
        self.radioButton_12 = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_12.setFont(font)
        self.radioButton_12.setObjectName("radioButton_12")
        self.horizontalLayout_2.addWidget(self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_13.setFont(font)
        self.radioButton_13.setObjectName("radioButton_13")
        self.horizontalLayout_2.addWidget(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_14.setFont(font)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_2.addWidget(self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.groupbox1)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_15.setFont(font)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_2.addWidget(self.radioButton_15)
        self.question3_layout.addWidget(self.groupbox1)
        self.gridLayout.addLayout(self.question3_layout, 2, 0, 1, 1)
        self.question4_layout = QtWidgets.QVBoxLayout()
        self.question4_layout.setContentsMargins(-1, 5, -1, 7)
        self.question4_layout.setObjectName("question4_layout")
        self.question4_text = QtWidgets.QLabel(self.questions_layout)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.question4_text.setFont(font)
        self.question4_text.setStyleSheet("")
        self.question4_text.setAlignment(QtCore.Qt.AlignCenter)
        self.question4_text.setObjectName("question4_text")
        self.question4_layout.addWidget(self.question4_text)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.plainText_answer = QtWidgets.QPlainTextEdit(self.questions_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plainText_answer.sizePolicy().hasHeightForWidth()
        )
        self.plainText_answer.setSizePolicy(sizePolicy)
        self.plainText_answer.setMinimumSize(QtCore.QSize(450, 100))
        self.plainText_answer.setMaximumSize(QtCore.QSize(500, 80))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(-1)
        self.plainText_answer.setFont(font)
        self.plainText_answer.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.plainText_answer.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.plainText_answer.setStyleSheet(
            "background-color: rgb(255, 255, 255);\n" "font-size: 20px;"
        )
        self.plainText_answer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plainText_answer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainText_answer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainText_answer.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents
        )
        self.plainText_answer.setObjectName("plainText_answer")
        self.horizontalLayout_4.addWidget(self.plainText_answer)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.question4_layout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.question4_layout, 3, 0, 1, 1)
        self.bottom_layout.addWidget(self.questions_layout)
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.button_layout.addItem(spacerItem2)
        self.submit_button = QtWidgets.QPushButton(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.submit_button.sizePolicy().hasHeightForWidth()
        )
        self.submit_button.setSizePolicy(sizePolicy)
        self.submit_button.setMinimumSize(QtCore.QSize(300, 0))
        self.submit_button.setMaximumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.submit_button.setFont(font)
        self.submit_button.setStyleSheet(
            "QPushButton{\n"
            "background-color:  rgb(255, 203, 99);\n"
            "border: none;\n"
            "border-radius: 5px;\n"
            "color: white;\n"
            "padding:32px;\n"
            "text-align: center;\n"
            "text-decoration: none;\n"
            "display: inline-block;\n"
            "font-size: 18px;\n"
            "}\n"
            "QPushButton:hover{\n"
            "background-color:  rgb(255, 220, 99);\n"
            "}"
        )
        self.submit_button.setObjectName("submit_button")
        self.button_layout.addWidget(self.submit_button)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.button_layout.addItem(spacerItem3)
        self.bottom_layout.addLayout(self.button_layout)
        self.gridLayout_3.addLayout(self.bottom_layout, 1, 0, 1, 1)
        self.logo_widget = QtWidgets.QWidget(self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_widget.sizePolicy().hasHeightForWidth())
        self.logo_widget.setSizePolicy(sizePolicy)
        self.logo_widget.setMaximumSize(QtCore.QSize(16777215, 200))
        self.logo_widget.setObjectName("logo_widget")
        self.logo_layout = QtWidgets.QHBoxLayout(self.logo_widget)
        self.logo_layout.setContentsMargins(-1, -1, -1, 1)
        self.logo_layout.setObjectName("logo_layout")
        self.app_logo = QtWidgets.QLabel(self.logo_widget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_logo.sizePolicy().hasHeightForWidth())
        self.app_logo.setSizePolicy(sizePolicy)
        self.app_logo.setMaximumSize(QtCore.QSize(610, 194))
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
        self.logo_layout.addWidget(self.app_logo)
        self.gridLayout_3.addWidget(self.logo_widget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.main_layout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.text1.setText(
            _translate(
                "Form",
                "On this page you will be asked 4 daily questions about your mental state.",
            )
        )
        self.text2.setText(
            _translate(
                "Form",
                "Your answers will be saved and protected. No one is able to see them.",
            )
        )
        self.question1_text.setText(_translate("Form", "Do you feel happy today?"))
        self.radioButton_3.setText(_translate("Form", "Very unhappy"))
        self.radioButton_4.setText(_translate("Form", "Unhappy"))
        self.radioButton.setText(_translate("Form", "Not clear"))
        self.radioButton_5.setText(_translate("Form", "Happy"))
        self.radioButton_2.setText(_translate("Form", "Very happy"))
        self.question2_text.setText(
            _translate("Form", "How satisfied are you with yourself today?")
        )
        self.radioButton_6.setText(_translate("Form", "Not at all satisfied"))
        self.radioButton_7.setText(_translate("Form", "Not satisfied"))
        self.radioButton_8.setText(_translate("Form", "Not clear"))
        self.radioButton_9.setText(_translate("Form", "Satisfied"))
        self.radioButton_10.setText(_translate("Form", "Very much satisfied"))
        self.question3_text.setText(_translate("Form", "How calm are you today?"))
        self.radioButton_11.setText(_translate("Form", "Not calm at all"))
        self.radioButton_12.setText(_translate("Form", "Not calm"))
        self.radioButton_13.setText(_translate("Form", "Not clear"))
        self.radioButton_14.setText(_translate("Form", "Calm"))
        self.radioButton_15.setText(_translate("Form", "Very calm"))
        self.question4_text.setText(
            _translate("Form", "Do you want to add anything? (Optional)")
        )
        self.submit_button.setText(_translate("Form", "Submit"))
        self.app_logo.setText(_translate("Form", "GoldApp"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
