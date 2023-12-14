# ----------------------- Modules ------------------------------ #
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from classes.DL.usersDL import UsersDL as dL
from classes.BL.Customers import Customer

# --------------------- Show Warning -------------------------- #
def show_Warning(self, message):
    QMessageBox.warning(self, "Warning", message)

# ------------------- Show Information ------------------------ #
def show_Information(self, message):
    QMessageBox.information(self, "Information", message)


#--------------- Taking Input from Sign Up page ----------------#
def TakeInput_SignIn(self):
    Name = self.findChild(QLineEdit, "signUp_userName").text()
    Password = self.findChild(QLineEdit, "signUp_passWord").text()
    email = self.findChild(QLineEdit, "signUp_email").text()
    address = self.findChild(QLineEdit, "signUp_address").text()
    
    if Name == "" or Password == "" or email == "" or address == "":
        show_Warning
        return
    else:
        user = Customer(Name, email, Password, address)
        dL.add_user(user)
        show_Information(self, "Sign Up Successful")
        self.changing_mainStack_PageNo(0)
        
        dL.store_in_csv()                        # Storing in csv file


# -------------------- Sign In Implementation ----------------- #
def TakeInput_LogIn(self):
    userName = self.findChild(QLineEdit, "userName").text()
    passWord = self.findChild(QLineEdit, "passWord").text()

    if userName == "" or passWord == "":
        show_Warning(self, "Please fill all the fields")
        return
    else:
        us = dL.get_user(userName)
        if us.data.username == userName and us.data.password == passWord:
            show_Information(self, "Sign In Successful")
            if type(us.data) == Customer:
                self.changing_mainStack_PageNo(4)
            else:
                self.changing_mainStack_PageNo(3)
        else:
            show_Warning(self, "Invalid Username or Password")
            return
        