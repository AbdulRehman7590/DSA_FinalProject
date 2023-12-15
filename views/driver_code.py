# ----------------------- Modules -------------------------------- #
import os,sys
# Change the path to the project root directory to import files from different folders
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(project_root)

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from utils.sign_In_Up import *
from utils.admin_options import *
from utils.cutomer_options import *

from classes.DL.usersDL import UsersDL as dL
from classes.DL.menu import Menu

from models.User_TableModel import UserTableModel
from models.Food_TableModel import FoodTableModel
from models.Order_TableModel import OrderTableModel

# ---------------------- Program -------------------------------- #
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("views/main.ui", self)


        # -------------------- Loading Data ---------------------- #
        dL.load_from_csv()
        Menu.load_from_csv()


        # ---------------------- Variables ----------------------- #
        self.path = ""
        self.about_pagerecord = -1
        self.users_columns = ["Name", "Email", "Address", "Type"]
        self.foods_columns = ["Food_Name", "Price", "Description", "Rating"]
        self.orders_columns = ["Order_ID", "Order_Status", "Order_Date", "Ordered_Items", "Order_Address", "Order_Total_Price"]


        # ------------------------ Tables ------------------------ #
        self.adminTable = self.findChild(QTableView,"admin_table")
        self.customerTable = self.findChild(QTableView,"customer_table")


        # ---------------------- Defaults ------------------------ #
        self.mainStack = self.findChild(QStackedWidget, "main_Stack")
        self.adminStack = self.findChild(QStackedWidget,"adminoption_stack")
        self.adminoption_stack = self.findChild(QStackedWidget,"admin_suboptions_stack")
        self.customerStack = self.findChild(QStackedWidget,"customerpages_stack")
        self.changing_mainStack_PageNo(0)


        # ------------------- Button Connections ----------------- #
        self.signUp_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(1))
        self.signin_about_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(2))
        self.login_Btn.clicked.connect(lambda: TakeInput_LogIn(self))
        self.back_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.register_Btn.clicked.connect(lambda: TakeInput_SignIn(self))
        self.signup_about_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(2))
        self.about_back_Btn.clicked.connect(self.back_from_about)


        # ---------------------- Admin Options ------------------------ #
        self.admin_logout_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.viewFood_Btn.clicked.connect(self.view_foods)
        self.viewOrders_Btn.clicked.connect(lambda: self.view_orders(dL.get_user(self.userName).all_orders_history))
        self.viewCustomers_Btn.clicked.connect(self.view_customers)
        self.viewStats_Btn.clicked.connect(lambda: showing_stats(self))
        self.addnew_Food_Btn.clicked.connect(lambda: self.changing_adminStack_PageNo(1))
        self.add_food_Btn.clicked.connect(lambda: add_new_food(self))
        self.uploadPhoto_Btn.clicked.connect(lambda: upload_photo(self))


        # -------------------- Customer Options ----------------------- #
        self.customer_logout_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.explore_Btn.clicked.connect(lambda: showing_explore_menu(self))
        self.fvt_Btn.clicked.connect(lambda: self.changing_customerStack_PageNo(3))
        self.cart_Btn.clicked.connect(lambda: self.changing_customerStack_PageNo(4))
        self.home_Btn.clicked.connect(lambda: self.changing_customerStack_PageNo(0))


    # ---------------------- Changing Page ------------------------ #
    def back_from_about(self):
        self.changing_mainStack_PageNo(self.about_pagerecord)

    def changing_mainStack_PageNo(self, index):
        if index == 2:
            self.about_pagerecord = self.mainStack.currentIndex()
        
        self.mainStack.setCurrentIndex(index)
        # Setting the pages 
        if index == 3:
            self.changing_adminStack_PageNo(0)
            self.view_foods()
        elif index == 4:
            self.changing_customerStack_PageNo(0)

    def changing_adminStack_PageNo(self, index):
        self.adminStack.setCurrentIndex(index)

    def changing_adminoption_stack_PageNo(self, index):
        self.adminoption_stack.setCurrentIndex(index)
        self.changing_adminStack_PageNo(0)

    def changing_customerStack_PageNo(self, index):
        self.customerStack.setCurrentIndex(index)


    # -------------------- Load admin Tables -------------------- #
    def view_foods(self):
        self.adminTable.setModel(FoodTableModel(Menu._food_list, self.foods_columns))
        header = self.adminTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.changing_adminoption_stack_PageNo(0)

    def view_orders(self,ordlist):
        self.adminTable.setModel(OrderTableModel(ordlist, self.orders_columns))
        header = self.adminTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.changing_adminoption_stack_PageNo(1)

    def view_customers(self):
        self.adminTable.setModel(UserTableModel(dL._user_list, self.users_columns))
        header = self.adminTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.changing_adminoption_stack_PageNo(2)


# ------------------------- Main --------------------------------- #
def Start():
    try:
        app = QApplication(sys.argv)
        window = Mainwindow()
        window.show()
        sys.exit(app.exec_())
        
    except Exception as e:
        print("An error occured: ", str(e))


if __name__ == "__main__":
    Start()
    