# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User

# ------------------------ Cook CLass ------------------------------ #
class Cook(User):
        def __init__(self,username,email,password,address,cook_id):
                super().__init__(username, email, password, address)

                self.__cook_id = cook_id
                self.__rating = 0
                self.__food_menu = None
                self.__order_list = None
                self.__delivered_orders = None
                self.__cancel_orders = None


        # ------------------------ Getter ------------------------------- #
        @property
        def cook_id(self):
                return self.__cook_id
        
        @property
        def rating(self):
                return self.__rating
        
        @property
        def food_menu(self):
                return self.__food_menu    
        
        @property
        def order_list(self):
                return self.__order_list
        
        @property
        def delivered_orders(self):
                return self.__delivered_orders
        
        @property
        def cancel_orders(self):
                return self.__cancel_orders
        
        
        # ------------------------ Setter ------------------------------- #
        @cook_id.setter
        def cook_id(self,cook_id):
                self.__cook_id = cook_id

        @rating.setter
        def rating(self,rating):
                self.__rating = rating % 5
        
        @food_menu.setter
        def food_menu(self,food_menu):
                self.__food_menu = food_menu

        @order_list.setter
        def order_list(self,order_list):
                self.__order_list = order_list
        
        @delivered_orders.setter
        def delivered_orders(self,delivered_orders):
                self.__delivered_orders = delivered_orders

        @cancel_orders.setter
        def cancel_orders(self,cancel_orders):
                self.__cancel_orders = cancel_orders


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