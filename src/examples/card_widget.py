from PyQt5 import QtCore, QtGui, QtWidgets
import os

path = os.path.dirname(os.path.abspath(__file__))


class card_widget(QtWidgets.QWidget):
    def widget_render(self):
        self.widget_2 = QtWidgets.QWidget()
        self.widget_2.setEnabled(True)
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 9, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.events_location = QtWidgets.QLabel(self.widget_2)
        self.events_location.setMinimumSize(QtCore.QSize(404, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.events_location.setFont(font)
        self.events_location.setStyleSheet("")
        self.events_location.setScaledContents(False)
        self.events_location.setAlignment(QtCore.Qt.AlignCenter)
        self.events_location.setObjectName("events_location")
        self.horizontalLayout.addWidget(self.events_location)


if __name__ == "__main__":
    import sys

    print(os.path.join(path, "chess.png"))

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = card_widget()
    ui.widget_render()
    ui.show()
    sys.exit(app.exec_())
