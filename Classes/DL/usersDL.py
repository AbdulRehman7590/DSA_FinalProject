# ------------------------ Libraries ------------------------------- #
from models.BST import BST
from classes.BL.Customers import Customer
from classes.BL.admin import Admin
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
        print("User added in BST")

    @staticmethod
    def remove_user(user):
        if UsersDL._user_list.deleteNode(user):
            print("User removed from BST")
        else:
            print("User not found in BST")

    @staticmethod
    def store_in_csv():
        users = UsersDL._user_list.preOrderTraversal(UsersDL._user_list.root)
        with open('inputs/user_data.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Email", "Password", "Address", "Type"])
            for user in users:
                writer.writerow([user.username, user.email, user.password, user.address, "Customer" if type(user) == Customer else "Admin"])

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
