# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User
from models.Hash_Table import HashTable
from models.Doubly_Linkedlist import DoubleLinkedList
from models.Stack import Stack
from models.Queue import Queue

from utils.sign_In_Up import show_Information,show_Warning

# --------------------- Customers CLass ---------------------------- #
class Customer(User):
        def __init__(self,username,email,password,address):
                super().__init__(username, email, password, address)

                self.__cart = DoubleLinkedList()
                self.__order_history = HashTable()
                self.__ordered_items_list = Queue()
                self.__delivered_order_list = Stack()
                self.__wishlist = DoubleLinkedList()

        # ------------------------ Getter ------------------------------ #
        @property
        def cart(self)->DoubleLinkedList:
                return self.__cart
        
        @property
        def order_history(self)->HashTable:
                return self.__order_history
        
        @property
        def ordered_items_list(self)->Queue:
                return self.__ordered_items_list
        
        @property
        def delivered_order_list(self)->Stack:
                return self.__delivered_order_list
        
        @property
        def wishlist(self)->DoubleLinkedList:
                return self.__wishlist
        
        # ------------------------ Methods ------------------------------ #
        def add_to_wishlist(self,item):
                if self.__wishlist.search_data(item.food_name):
                        show_Warning(f"{item.food_name} already stored in wishlist")
                else:
                        self.__wishlist.insert_at_tail(item)
                        show_Information(f"{item.food_name} stored in wishlist")

        def remove_from_wishlist(self,item):
                self.__wishlist.delete_data(item)
                show_Information(f"{item.food_name} removed from wishlist")

        def add_to_cart(self,item):
                self.__cart.insert_at_tail(item)
                show_Information(f"{item.food_name} stored in cart")

        def remove_from_cart(self,item):
                self.__cart.delete_data(item)
                show_Information(f"{item.food_name} removed from cart")

        def add_to_ordered_items_list(self,item):
                self.__order_history.insert(item)
                print("item stored in order history")
                self.__ordered_items_list.enqueue(item)
                show_Information(f"{item.food_name} stored in ordered items list")
                self.remove_from_cart(item)
                print("item removed from cart")

        def add_to_delivered_order_list(self):
                self.__delivered_order_list.push(self.__ordered_items_list.dequeue())
                print("item stored in delivered order list")

