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
        if dL.get_user(Name) == None:
            dL.add_user(user)
            self.show_Information("Sign Up Successful")
            self.changing_mainStack_PageNo(0)
            dL.store_in_csv()                        # Storing in csv file
        else:
            self.show_Warning("User already exists")
        


# -------------------- Sign In Implementation ----------------- #
def TakeInput_LogIn(self):
    userName = self.findChild(QLineEdit, "userName").text()
    passWord = self.findChild(QLineEdit, "passWord").text()

    if userName == "" or passWord == "":
        self.show_Warning("Please fill all the fields")
        return
    else:
        us = dL.get_user(userName)
        if us is not None and us.username == userName and us.password == passWord:
            self.user = us
            self.show_Information("Sign In Successful")
            self.userName.setText("")
            self.passWord.setText("")
            if type(us) == Customer:
                self.changing_mainStack_PageNo(4)
            else:
                self.changing_mainStack_PageNo(3)
        else:
            self.show_Warning("Invalid Username or Password")
            return
        