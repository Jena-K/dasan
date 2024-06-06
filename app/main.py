import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from dasan_main_ui import Ui_MainWindow
from sub01_ui import Ui_B1_Action
# 위젯 선언
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.button_01.clicked.connect(self.show_popup)  # Connect the button click to the show_popup method

    def show_popup(self):
        self.popup = Popup()  # Create an instance of the Popup class
        self.popup.show()  # Show the popup window


class Popup(QtWidgets.QMainWindow, Ui_B1_Action):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI from Designer


# 어플리케이션 호출 및 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    