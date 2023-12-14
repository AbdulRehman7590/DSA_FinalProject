# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User
from models.Hash_Table import HashTable
from models.Doubly_Linkedlist import DoubleLinkedList
from models.Stack import Stack
from models.Queue import Queue

# --------------------- Customers CLass ---------------------------- #
class Customer(User):
        def __init__(self,username,email,password,address):
                super().__init__(username, email, password, address)

                self.__cart = HashTable()
                self.__order_history = HashTable()
                self.__ordered_items_list = Queue()
                self.__delivered_order_list = Stack()
                self.__wishlist = DoubleLinkedList()

        # ------------------------ Getter ------------------------------ #
        @property
        def cart(self)->HashTable:
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
                self.__wishlist.append(item)

        def remove_from_wishlist(self,item):
                self.__wishlist.remove(item)

        def add_to_cart(self,item):
                self.__cart.insert(item)

        def remove_from_cart(self,item):
                self.__cart.remove(item)

        def add_to_ordered_items_list(self,item):
                self.__order_history.insert(item)
                self.__ordered_items_list.enqueue(item)
                self.remove_from_cart(item)

        def add_to_delivered_order_list(self):
                self.__delivered_order_list.push(self.__ordered_items_list.dequeue())

        def remove_from_delivered_order_list(self):
                self.__delivered_order_list.pop()
