
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from dasan_main_ui import Ui_MainWindow
import account_ui
# 위젯 선언
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        
        self.ui_main.button_popup_accnt.clicked.connect(self.show_popup)  # Connect the button click to the show_popup method

    def show_popup(self):
        self.popup = Popup()  # Create an instance of the Popup class
        self.popup.exec()  # Show the popup window




# class Popup(QtWidgets.QMainWindow, manage_account_ui.Ui_MainWindow):
class Popup(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui_accnt = account_ui.Ui_Dialog()
        self.ui_accnt.setupUi(self)  # Set up the UI from Designer

    def resizeRowsToContents(self, row):
        print(1)
        # tbview_model = self.ui_accnt.tableWidget;
        # # Add an empty row to the model
        # tbview_model.appendRow([QtGui.QStandardItem("") for _ in range(tbview_model.columnCount())])
        # # Select the newly added row for user convenience
        # tbview_model.selectRow(tbview_model.rowCount() - 1)

# 어플리케이션 호출 및 실행
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
    