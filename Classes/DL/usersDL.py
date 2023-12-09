# ------------------------ Libraries ------------------------------- #
import typing
from classes.BL.users import User
from models.Doubly import DoubleLinkedList


# ------------------------ UserDL ------------------------------- #
class UsersDL():
    def __init__(self):
            self.__user_list = DoubleLinkedList()
    
    # ------------------------ Getter ------------------------------ #
    @property
    def user_list(self):
            return self.__user_list


    # ------------------------ Methods ------------------------------ #
    def add_user(self,user):
            pass
    
    def remove_user(self,user):
            pass

    def display_users(self):
            pass
    
    def search_user_by_name(self,user_name):
            pass
    
    def search_user_by_email(self,user_email):
            pass