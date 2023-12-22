# ------------------------ Libraries ------------------------------- #
from models.Linkedlist import LinkedList
from Classes.BL.foods import Food
import csv

# ------------------------ Menu CLass ------------------------------ #
class Menu():
        _food_list = LinkedList()
        
        # --------------------- Methods ---------------------------- #
        @staticmethod
        def add_food(food):
                if Menu._food_list.search_data(food.food_name):
                        print("Food already exists in DLL")
                        return False
                else:
                        Menu._food_list.insert_at_tail(food)
                        print("Food added in DLL")
                        return True
        
        @staticmethod
        def remove_food(food):
                if Menu._food_list.delete_node(food):
                        print("Food deleted from DLL")
                else:
                        print("Food not found in DLL")
        
        @staticmethod
        def search_food(foodname):
                return Menu._food_list.search_data(foodname)
        
        @staticmethod
        def store_in_csv():
                with open('inputs/food_data.csv', 'w', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(["Item_Name", "Price", "Description", "Rating"])
                        temp = Menu._food_list.head
                        while temp is not None:
                                writer.writerow([temp.data.food_name, temp.data.food_price, temp.data.food_description, temp.data.food_rating, temp.data.food_likes])
                                temp = temp.next

        @staticmethod
        def load_from_csv():
                with open('inputs/food_data.csv', 'r') as file:
                        reader = csv.reader(file)
                        
                        try:
                                next(reader)
                                for row in reader:
                                        if row:
                                                food = Food(row[0], row[1], f"views/Images/{row[0]}.jpg", row[2], int(row[3]))
                                                food.food_likes = int(row[4])
                                                Menu._food_list.insert_at_tail(food)
                        except Exception as e:
                                print(f"An error occurred: {e}")
