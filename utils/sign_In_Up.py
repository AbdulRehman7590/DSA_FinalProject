# ----------------------- Modules ------------------------------ #
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from classes.DL.usersDL import UsersDL as dL
from classes.BL.Customers import Customer


#--------------- Taking Input from Sign Up page ----------------#
def TakeInput_SignIn(self):
    Name = self.findChild(QLineEdit, "signUp_userName").text()
    Password = self.findChild(QLineEdit, "signUp_passWord").text()
    email = self.findChild(QLineEdit, "signUp_email").text()
    address = self.findChild(QLineEdit, "signUp_address").text()
    
    if Name == "" or Password == "" or email == "" or address == "":
        self.show_Warning("Please fill all the fields")
        return
    else:
        user = Customer(Name, email, Password, address)
        dL.add_user(user)
        self.show_Information("Sign Up Successful")
        self.changing_mainStack_PageNo(0)
        
        dL.store_in_csv()                        # Storing in csv file


# -------------------- Sign In Implementation ----------------- #
def TakeInput_LogIn(self):
    self.userName = self.findChild(QLineEdit, "userName").text()
    self.passWord = self.findChild(QLineEdit, "passWord").text()

    if self.userName == "" or self.passWord == "":
        self.show_Warning("Please fill all the fields")
        return
    else:
        us = dL.get_user(self.userName)
        if us.data.username == self.userName and us.data.password == self.passWord:
            self.user = us.data
            self.show_Information("Sign In Successful")
            if type(us.data) == Customer:
                self.changing_mainStack_PageNo(4)
            else:
                self.changing_mainStack_PageNo(3)
        else:
            self.show_Warning("Invalid Username or Password")
            return
        