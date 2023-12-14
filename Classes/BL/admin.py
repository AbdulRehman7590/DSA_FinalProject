# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User
from models.Stack import Stack
from models.Queue import Queue
from models.Hash_Table import HashTable

# ------------------------ Cook CLass ------------------------------ #
class Admin(User):
        def __init__(self,username,email,password,address):
                super().__init__(username, email, password, address)

                self.__all_orders_history = HashTable()
                self.__pending_orders = Queue()
                self.__delivered_orders = Stack()
                self.__cancel_orders = HashTable()

        # ------------------------ Getter ------------------------------ #
        @property
        def all_orders_history(self)->HashTable:
                return self.__all_orders_history
        
        @property
        def pending_orders(self)->Queue:
                return self.__pending_orders
        
        @property
        def delivered_orders(self)->Stack:
                return self.__delivered_orders
        
        @property
        def cancel_orders(self)->HashTable:
                return self.__cancel_orders
        
        # ------------------------ Methods ------------------------------ #
        def add_order(self,order):
                self.__all_orders_history.insert(order)
                self.__pending_orders.enqueue(order)
        
        def add_delivered_order(self,order):
                self.__pending_orders.dequeue()
                self.__delivered_orders.push(order)
        
        def add_cancel_order(self):
                self.__cancel_orders.insert(self.__pending_orders.dequeue())

        def remove_cancel_order(self,order):
                self.__cancel_orders.remove(order)
                self.__pending_orders.enqueue(order)

        def remove_order(self,order):
                self.__all_orders_history.remove(order)
                self.__pending_orders.dequeue()
