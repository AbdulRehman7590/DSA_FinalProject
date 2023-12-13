# ----------------------- Modules -------------------------------- #
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# ---------------------- Food Tab ------------------------------- #
def add_food_tab(food):
    main_widget = QWidget()
    main_layout = QVBoxLayout()

    label = QLabel()
    pixmap = QPixmap(food.food_img_path)
    label.setPixmap(pixmap)
    main_layout.addWidget(label)
    
    inner_widget = QGroupBox("Inner Widget")
    inner_layout = QGridLayout()
    
    label1 = QLabel(food.food_name)
    label2 = QLabel(food.food_price)
    
    button1 = QPushButton()
    button1.setIcon(QtGui.QIcon("views/Icons & logos/add_fvt.png"))
    button1.styleSheet = {"background-color:rgb(244,244,244); \n border-radius:10%;"}
    
    button2 = QPushButton()
    button2.setIcon(QtGui.QIcon("views/Icons & logos/add_cart.png"))
    button2.styleSheet = {"background-color:rgb(244,244,244); \n border-radius:10%;"}

    inner_layout.addWidget(label1, 0, 0)
    inner_layout.addWidget(label2, 0, 1)
    inner_layout.addWidget(button1, 1, 0)
    inner_layout.addWidget(button2, 1, 1)

    inner_widget.setLayout(inner_layout)
    main_layout.addWidget(inner_widget)
    main_widget.setLayout(main_layout)
    return main_widget
