import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import csv
import time
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi(r"D:\DSAFinalProject\cs261f23pid28\views\Check.ui", self)
      

        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())