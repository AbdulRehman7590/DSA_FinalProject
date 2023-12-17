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
                if self.__wishlist.search_data(item.food_name) is None:
                        self.__wishlist.insert_at_tail(item)
                        print(f"{item.food_name} stored in wishlist")
                        return True
                else:
                        print(f"{item.food_name} already stored in wishlist")
                        return False

        def remove_from_wishlist(self,item):
                if self.__wishlist.search_data(item.food_name) is not None:
                        self.__wishlist.delete_data(item)
                        print("item removed from wishlist")
                        return True
                else:
                        print("item not found in wishlist")
                        return False

        def add_to_cart(self,item):
                if self.__cart.search(item.order_id) is None:
                        self.__cart.insert(item)
                        print("item stored in cart")
                        return True
                else:
                        print("item already stored in cart")
                        return False

        def remove_from_cart(self,item):
                if self.__cart.search(item.order_id):
                        self.__cart.remove(item)
                        print("item removed from cart")
                        return True
                else:
                        print("Item not found in cart")
                        return False

        def add_to_ordered_items_list(self,item):
                self.__order_history.insert(item)
                print("item stored in order history")
                self.__ordered_items_list.enqueue(item)
                print("item stored in ordered items list")
                self.remove_from_cart(item)
                print("item removed from cart")

        def add_to_delivered_order_list(self):
                self.__delivered_order_list.push(self.__ordered_items_list.dequeue())
                print("item stored in delivered order list")

