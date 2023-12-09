import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import time
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow,self).__init__()
<<<<<<< HEAD
        loadUi("views/SignUp.ui",self)
        
        
=======
        loadUi("trial.ui",self)
    #     #self.SignInButton.clicked.connect(lambda: self.toggle_ui(0))
    #     #self.SignUpButton.clicked.connect(lambda: self.toggle_ui(1))
    # def toggle_ui(self, index):
    #     self.main_Stack.setCurrentIndex(index)
     
>>>>>>> f73d2a6d88edc4044ccc4e60bd9ce72c061851ad
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())