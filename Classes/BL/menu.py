# ------------------------ Libraries ------------------------------- #
from classes.BL.foods import Food

import os,sys
# Change the path to the project root directory to import files from different folders
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(project_root)

from models.Doubly import DoubleLinkedList

# ------------------------ Menu CLass ------------------------------ #
class Menu():
        def __init__(self):
                self.__food_list = DoubleLinkedList()
        
        # ------------------------ Getter ------------------------------ #
        @property
        def food_list(self):
                return self.__food_list
        
        # ------------------------ Setter ------------------------------ #
        @food_list.setter
        def food_list(self,food_list):
                self.__food_list = food_list


        # ------------------------ Methods ------------------------------ #
        def add_food(self,food):
                self.food_list.insert_at_tail(food)
        
        def remove_food(self,food):
                self.food_list.remove(food)

        def display_food(self):
                self.food_list.display()
        
        def search_food(self,food):
                return self.food_list.search(food)
        
