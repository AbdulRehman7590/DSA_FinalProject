# ------------------------ Libraries ------------------------------- #
from Classes.BL.foods import Food
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
        def add_food(self):
                food = Food()
                self.food_list.insert_at_tail(food)
        
        def remove_food(self):
                food = Food()
                self.food_list.remove(food)

        def display_food(self):
                self.food_list.display()
        
        def search_food(self):
                food = Food()
                return self.food_list.search(food)
        
