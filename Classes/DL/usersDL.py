# ------------------------ Libraries ------------------------------- #
import typing
from models.Doubly import DoubleLinkedList
from models.BST import BST
from classes.BL.users import User


# ------------------------ UserDL ------------------------------- #
class UsersDL():
    _user_bst = BST()
    
    # ------------------------ Methods ------------------------------ #
    @staticmethod
    def get_user_list():
        return UsersDL._user_list


    @staticmethod
    def add_user(user):
        UsersDL._user_bst.insert(None,user)
        print("Entered in DL happily")
    
    @staticmethod
    def remove_user(user):
        pass

    @staticmethod
    def display_users():
        pass
    
    @staticmethod
    def search_user_by_name(user_name):
        pass
    
    @staticmethod
    def search_user_by_email(user_email):
        pass
    
