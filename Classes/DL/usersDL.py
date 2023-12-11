# ------------------------ Libraries ------------------------------- #
import typing
from classes.BL.users import User
from models.Doubly import DoubleLinkedList


# ------------------------ UserDL ------------------------------- #
class UsersDL():
    _user_list = DoubleLinkedList()
    
    # ------------------------ Methods ------------------------------ #
    @staticmethod
    def get_user_list():
        return UsersDL._user_list


    @staticmethod
    def add_user(user):
        pass
    
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