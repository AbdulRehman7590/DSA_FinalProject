from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.DL.usersDL import UsersDL as dL
from Classes.BL.Customers import Customer

#----------------- Taking Input from Sign Up page --------------#
def TakeInput_SignIn(self):
    Name = self.findChild(QLineEdit, "signUp_userName").text()
    Password = self.findChild(QLineEdit, "signUp_passWord").text()
    email = self.findChild(QLineEdit, "signUp_email").text()
    address = self.findChild(QLineEdit, "signUp_address").text()
    
    if Name == "" or Password == "" or email == "" or address == "":
        QMessageBox.warning(self, "Warning", "Please fill all the fields")
        return
    else:
        user = Customer(Name, email, Password, address)
        dL.add_user(user)
        QMessageBox.information(self, "Information", "User Added Successfully")
        self.changing_mainStack_PageNo(0)
        
        dL.store_in_csv()                        # Storing in csv file


# -------------------- Sign In Implementation ----------------- #
def TakeInput_LogIn(self):
    dL.load_from_csv()                          # Loading from csv file

    userName = self.findChild(QLineEdit, "userName").text()
    passWord = self.findChild(QLineEdit, "passWord").text()

    if userName == "" or passWord == "":
        QMessageBox.warning(self, "Warning", "Please fill all the fields")
        return
    else:
        us = dL.get_user(userName)
        if us.data.username == userName and us.data.password == passWord:
            QMessageBox.information(self, "Information", "Login Successful")
            if us.data is Customer:
                self.changing_mainStack_PageNo(4)
            else:
                self.changing_mainStack_PageNo(3)
        else:
            QMessageBox.warning(self, "Warning", "Invalid Username or Password")
            return
        