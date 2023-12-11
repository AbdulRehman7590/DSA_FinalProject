# ----------------------- Modules -------------------------------- #
import sys, os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from Classes.DL.usersDL import usersDL

import os,sys
# Change the path to the project root directory to import files from different folders
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(project_root)

# ---------------------- Program -------------------------------- #
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("views/main.ui", self)
        self.pushButton.clicked.connect(self.TakeInput)
        usersDL.add_user()
        
        


        # ---------------------- Defaults ------------------------ #
        self.mainStack = self.findChild(QStackedWidget, "main_Stack")
        self.changing_PageNo(0)


        # ------------------- Button Connections ------------------ #
        self.back_Btn.clicked.connect(lambda: self.changing_PageNo(0))
        self.login_Btn.clicked.connect(lambda: self.changing_PageNo(0))
        self.signUp_Btn.clicked.connect(lambda: self.changing_PageNo(1))
        self.about_Btn.clicked.connect(lambda: self.changing_PageNo(2))
        self.about_Btn_2.clicked.connect(lambda: self.changing_PageNo(2))


        # ------------------- Button Functions -------------------- #
    def changing_PageNo(self, index):
        self.mainStack.setCurrentIndex(index)
        
        
        
        
        #------------------- Taking Input from Sign Up page --------------#
        
    def TakeInput(self):
        Name = self.signUp_userName.text()
        Password = self.signUp_passWord.text()
        email = self.signUp_email.text()
        address = self.signUp_address.text()
        
        # Assuming your User class is defined in usersDL module
        user = user(Name, email, Password, address)

        # Add the user to the UsersDL
        usersDL.add_user(user)
        return user
        


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
    
