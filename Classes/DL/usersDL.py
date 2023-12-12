# ------------------------ Libraries ------------------------------- #
from models.BST import BST
from Classes.BL.Customers import Customer
from Classes.BL.admin import Admin
import csv


# ------------------------ UserDL ------------------------------- #
class UsersDL():
    _user_list = BST()
    
    # ------------------------ Methods ------------------------------ #
    @staticmethod
    def get_user(username):
        return UsersDL._user_list.findNode(username)

    @staticmethod
    def add_user(user):
        UsersDL._user_list.insertNode(user)
        print("Entered in DL happily")
            
    
    @staticmethod
    def remove_user(user):
        pass

    @staticmethod
    def store_in_csv():
        UsersDL._user_list.inOrderTraversal(UsersDL._user_list.root)

    @staticmethod
    def load_from_csv():
        with open('inputs/user_data.csv', 'r') as file:
            reader = csv.reader(file)
            try:
                next(reader)
                for row in reader:
                    if row:
                        if row[4] == "Admin":
                            user = Admin(row[0], row[1], row[2], row[3])
                        else:
                            user = Customer(row[0], row[1], row[2], row[3])
                        UsersDL._user_list.insertNode(user)
                        
            except Exception as e:
                print(f"An error occurred: {e}")
