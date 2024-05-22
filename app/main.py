# import tkinter as tk
# from tkinter import ttk, messagebox
# import pandas as pd

# class DataTransferApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Data Transfer App")
#         self.create_widgets()
#         self.load_data()

#     def create_widgets(self):
#         # Frames
#         self.left_frame = ttk.Frame(self.root)
#         self.left_frame.grid(row=0, column=0, padx=30, pady=10)
#         self.right_frame = ttk.Frame(self.root)
#         self.right_frame.grid(row=0, column=2, padx=30, pady=10)
#         self.button_frame = ttk.Frame(self.root)
#         self.button_frame.grid(row=0, column=1, padx=10, pady=10)
#         self.save_frame = ttk.Frame(self.root)
#         self.save_frame.grid(row=1, column=0, columnspan=3, pady=10)

#         # Treeviews
#         self.left_tree = ttk.Treeview(self.left_frame, columns=("Data"), show='headings')
#         self.left_tree.heading("Data", text="Data")
#         self.left_tree.pack()

#         self.right_tree = ttk.Treeview(self.right_frame, columns=("Data"), show='headings')
#         self.right_tree.heading("Data", text="Data")
#         self.right_tree.pack()

#         # Buttons
#         self.transfer_button = ttk.Button(self.button_frame, text=">", command=self.transfer_data)
#         self.transfer_button.pack(pady=20)

#         self.save_button = ttk.Button(self.save_frame, text="Save", command=self.save_data)
#         self.save_button.pack()

#     def load_data(self):
#         # Try different encodings until you find the one that works
#         try:
#             self.df = pd.read_csv('data.csv', encoding='utf-8')
#         except UnicodeDecodeError:
#             print("Unable to read using UTF-8 encoding. Trying different encodings...")
#             try_encodings = ['utf-8-sig', 'euc-kr', 'utf-8-BOM', 'cp-949']
#             for encoding in try_encodings:
#                 try:
#                     self.df = pd.read_csv('data.csv', encoding=encoding)
#                     print(f"Successfully read using {encoding} encoding.")
#                     break
#                 except UnicodeDecodeError:
#                     print(f"Failed to read using {encoding} encoding.")
#             else:
#                 raise Exception("Unable to read the file with any encoding.")
#         for index, row in self.df.iterrows():
#                 self.left_tree.insert("", "end", values=(row[0],))
                
#     def transfer_data(self):
#         selected_item = self.left_tree.selection()
#         if selected_item:
#             item_data = self.left_tree.item(selected_item, 'values')
#             self.right_tree.insert("", "end", values=item_data)

#     def save_data(self):
#         right_data = [self.right_tree.item(item, 'values')[0] for item in self.right_tree.get_children()]
#         if right_data:
#             pd.DataFrame(right_data).to_csv('data_new.csv', index=False, header=False)
#             messagebox.showinfo("Success", "Data saved to data_new.csv.")
#         else:
#             messagebox.showwarning("Warning", "No data to save.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = DataTransferApp(root)
#     root.mainloop()



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
    