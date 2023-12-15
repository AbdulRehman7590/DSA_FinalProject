# ----------------------- Modules ------------------------------ #
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from utils.sign_In_Up import show_Warning, show_Information
from classes.BL.foods import Food
from classes.DL.menu import Menu

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# --------------------- Admin Options -------------------------- #
def upload_photo(self):
        self.path , _ = QFileDialog.getOpenFileName(self, "Upload food image", "","")


# -------------------- Add foodin list ------------------------- #
def add_new_food(self):
    food_name = self.findChild(QLineEdit, "food_name").text()
    food_price = self.findChild(QLineEdit, "food_price").text()
    food_description = self.findChild(QLineEdit, "food_description").text()
    image_path = self.path

    if food_name == "" or food_price == "" or food_description == "" or image_path == "":
        show_Warning(self, "Please fill all the fields")
        
    else:
        food = Food(food_name, food_price, image_path, food_description, 0)
        Menu.add_food(food)
        show_Information(self, "Food Added Successfully")
        self.view_foods()
        
        Menu.store_in_csv()


def showing_stats(self):
    self.changing_adminStack_PageNo(2)

    self.horizontal_layout = QHBoxLayout(self.findChild(QWidget, "data_stats"))
    self.figure = plt.figure(figsize=(15, 5))
    self.canvas = FigureCanvas(self.figure)
    self.horizontal_layout.addWidget(self.canvas)
    
    self.figure.clear()

    self.ax = self.figure.add_subplot(111)
    self.ax.set_title("Food Rating Stats")
    self.ax.set_xlabel("Food Name")
    self.ax.set_ylabel("Food Rating")
    self.ax.grid(True)
    self.ax.set_ylim(0, 5)
    self.ax.set_yticks([0, 1, 2, 3, 4, 5])
    self.ax.set_xticks([])
    self.ax.set_xticklabels([])
    self.ax.set_yticklabels([0, 1, 2, 3, 4, 5])
    self.ax.spines['top'].set_visible(True)
    self.ax.spines['right'].set_visible(True)
    self.ax.spines['bottom'].set_visible(True)
    self.ax.spines['left'].set_visible(True)
    self.canvas.draw()

    self.foods = Menu._food_list.head
    self.food_names = []
    self.food_ratings = []
    while self.foods is not None:
        self.food_names.append(self.foods.data.food_name)
        self.food_ratings.append(self.foods.data.food_rating)
        self.foods = self.foods.next

    self.ax.bar(self.food_names, self.food_ratings, color="green")
    self.canvas.draw()
    

