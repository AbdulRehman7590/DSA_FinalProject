# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User

# ----------------------- Riders CLass ----------------------------- #
class Rider(User):
        def __init__(self,username,email,password,address,rider_id):
                super().__init__(username, email, password, address)
                
                self._rider_id = rider_id
                self._is_available = True
                self._order_list = None


        # ------------------------ Methods ------------------------------ #
        def view_all_orders(self):
                pass

        def view_all_delivered_orders(self):
                pass

        def view_all_pending_orders(self):
                pass

        def view_all_orders_by_address(self):
                pass

        def view_order(self,order_id):
                pass

        def view_profile(self):
                return super().view_profile()