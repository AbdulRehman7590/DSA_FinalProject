# ------------------------ Libraries ------------------------------- #
from classes.BL.users import User

# ----------------------- Admin CLass ------------------------------ #
class Admin(User):
        def __init__(self,username,email,password,address,rides_list,cooks_list,customers_list):
                super().__init__(username, email, password, address)

                self.__rides_list = rides_list
                self.__cooks_list = cooks_list
                self.__customers_list = customers_list


        # ------------------------ Getter ------------------------------- #
        @property
        def rides_list(self):
                return self.__rides_list
        
        @property
        def cooks_list(self):
                return self.__cooks_list
        
        @property
        def customers_list(self):
                return self.__customers_list
        

        # ------------------------ Setter ------------------------------- #
        @rides_list.setter
        def rides_list(self,rides_list):
                self.__rides_list = rides_list

        @cooks_list.setter
        def cooks_list(self,cooks_list):
                self.__cooks_list = cooks_list

        @customers_list.setter
        def customers_list(self,customers_list):
                self.__customers_list = customers_list


        # ------------------------ Methods ------------------------------ #
        def view_all_riders(self):
                pass

        def view_all_cooks(self):
                pass

        def view_all_customers(self):
                pass

        def view_profile(self):
                return super().view_profile()


