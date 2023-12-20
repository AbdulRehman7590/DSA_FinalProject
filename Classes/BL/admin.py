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
                print("Order Added in history")
                self.__pending_orders.enqueue(order)
                print("Order Added in pending")
        
        def add_delivered_order(self):
                order = self.__pending_orders.dequeue()
                print("Order Removed from pending")
                self.__delivered_orders.push(order)
                print("Order Added in delivered")
                order.order_name.add_to_delivered_order_list()
                print("Order Added in Customer delivered list")
        
        def remove_order(self,order):
                self.__all_orders_history.remove(order)
                print("Order Removed from history")
                self.__pending_orders.dequeue()
                print("Order Removed from pending")
