from LoginScreen.LoginScreen import LoginScreen
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

sys.path.insert(0, "../src")


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
