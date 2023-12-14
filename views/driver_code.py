# ----------------------- Modules -------------------------------- #
import os,sys
# Change the path to the project root directory to import files from different folders
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(project_root)

from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from utils.sign_In_Up import *
from classes.DL.usersDL import UsersDL as dL

# ---------------------- Program -------------------------------- #
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("views/main.ui", self)


        # -------------------- Loading Data ---------------------- #
        dL.load_from_csv()



        # ---------------------- Defaults ------------------------ #
        self.mainStack = self.findChild(QStackedWidget, "main_Stack")
        self.adminStack = self.findChild(QStackedWidget,"adminoption_pages")
        self.customerStack = self.findChild(QStackedWidget,"customerpages_stack")
        self.changing_mainStack_PageNo(0)
        self.changing_adminStack_PageNo(0)
        self.changing_customerStack_PageNo(0)


        # ------------------- Button Connections ------------------ #
        self.back_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.login_page_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.signUp_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(1))
        self.about_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(2))
        self.about_Btn_2.clicked.connect(lambda: self.changing_mainStack_PageNo(2))
        self.register_Btn.clicked.connect(lambda: TakeInput_SignIn(self))
        self.login_Btn.clicked.connect(lambda: TakeInput_LogIn(self))
        self.logout_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.logout_Btn_2.clicked.connect(lambda: self.changing_mainStack_PageNo(0))


    # ---------------------- Changing Page ------------------------ #
    def changing_mainStack_PageNo(self, index):
        self.mainStack.setCurrentIndex(index)

    def changing_adminStack_PageNo(self, index):
        self.adminStack.setCurrentIndex(index)

    def changing_customerStack_PageNo(self, index):
        self.customerStack.setCurrentIndex(index)


# ------------------------- Main --------------------------------- #
def Start():
    try:
        app = QApplication(sys.argv)
        window = Mainwindow()
        window.show()
        sys.exit(app.exec_())
        
    except Exception as e:
        print("An error occured: ", str(e))


if __name__ == "__main__":
    Start()
    