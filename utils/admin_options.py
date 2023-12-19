# ----------------------- Modules ------------------------------ #
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from classes.BL.foods import Food
from classes.DL.menu import Menu
from utils.algorithms import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# --------------------- Admin Options -------------------------- #
def upload_photo(self):
        path , _ = QFileDialog.getOpenFileName(self, "Upload food image", "","")
        self.food_img_path = path.split("/")[-1]
        print(self.food_img_path)


# -------------------- Add foodin list ------------------------- #
def add_new_food(self):
    food_name = self.findChild(QLineEdit, "food_name").text()
    food_price = self.findChild(QLineEdit, "food_price").text()
    food_description = self.findChild(QLineEdit, "food_description").text()
    
    image_path = f"views/Images/{self.food_img_path}"

    if food_name == "" or food_price == "" or food_description == "" or image_path == "":
        self.show_Warning("Please fill all the fields")
        
    else:
        food = Food(food_name, food_price, image_path, food_description, 0)
        if Menu.add_food(food):
            self.show_Information("Food Added Successfully")
        else:
            self.show_Warning("Food already exists")
        self.view_foods()
        
        Menu.store_in_csv()


# ------------------- View food stats --------------------------- #
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

    foods = Menu._food_list.head
    food_names = []
    food_ratings = []
    while foods is not None:
        food_names.append(foods.data.food_name)
        food_ratings.append(foods.data.food_rating)
        foods = foods.next

    self.ax.bar(food_names, food_ratings, color="green")
    self.canvas.draw()


#----------------------------- Sort Data --------------------------#
def Sort(self):
    print("Entered")
    # temp = Menu._food_list.head
    # while temp is not None:
    #     print(f"Food Name: {temp.data.food_name}, Price: {temp.data.food_price}, Description: {temp.data.food_description}, Rating: {temp.data.food_rating}")
    #     temp = temp.next

    column = 1  # Change this to the appropriate column index
    print(column)
    Menu._food_list = Algo.mergeSort(self,Menu._food_list.head)

    print("Sorted list:")
    temp = Menu._food_list.head
    while temp is not None:
        print(f"Food Name: {temp.data.food_name}, Price: {temp.data.food_price}")
        temp = temp.next

    
    print("Sorting done")
    
