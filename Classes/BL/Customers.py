# ------------------------ Libraries ------------------------------- #
from classes.BL.Users import User

# --------------------- Customers CLass ---------------------------- #
class Customer(User):
        def __init__(self,username,email,password,address):
                super().__init__(username, email, password, address)

                self.__cart = None
                self.__order_history = None
                self.__received_order_list = None
                self.__wishlist = None


        # ------------------------ Getter ------------------------------- #
        @property
        def cart(self):
                return self.__cart
        
        @property
        def order_history(self):
                return self.__order_history
        
        @property
        def received_order_list(self):
                return self.__received_order_list
        
        @property
        def wishlist(self):
                return self.__wishlist


        # ------------------------ Setter ------------------------------- #
        @received_order_list.setter
        def received_order_list(self,received_order_list):
                self.__received_order_list = received_order_list

        @wishlist.setter
        def wishlist(self,wishlist):
                self.__wishlist = wishlist
        
        @cart.setter
        def cart(self,cart):
                self.__cart = cart
        
        @order_history.setter
        def order_history(self,order_history):
                self.__order_history = order_history


        # ------------------------ Methods ------------------------------ #
        def view_all_orders(self):
                pass

        def view_all_delivered_orders(self):
                pass

        def view_all_pending_orders(self):
                pass

        def view_all_cancelled_orders(self):
                pass

        def view_all_orders_by_date(self):
                pass

        def view_profile(self):
                return super().view_profile()

