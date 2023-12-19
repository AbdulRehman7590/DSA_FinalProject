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
        self.food_img_path = ""
        self.about_pagerecord = -1
        self.back_from_cart = -1
        self.tab_item = ""
        self.like_bton = 0


        # ---------------------- Columns ------------------------- #
        self.users_columns = ["Name", "Email", "Address", "Type"]
        self.foods_columns = ["Food_Name", "Price", "Description", "Rating", "Likes"]
        self.orders_columns = ["Order_ID", "Order_Date", "Order_Address", "Order_Item", "Order_Quantity", "Order_Total_Price"]


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
        self.viewOrders_Btn.clicked.connect(lambda: self.view_orders(self.user.all_orders_history, self.adminTable))
        self.viewCustomers_Btn.clicked.connect(self.view_customers)
        self.viewStats_Btn.clicked.connect(lambda: showing_stats(self))
        self.addnew_Food_Btn.clicked.connect(lambda: self.changing_adminStack_PageNo(1))
        self.add_food_Btn.clicked.connect(lambda: add_new_food(self))
        self.uploadPhoto_Btn.clicked.connect(lambda: upload_photo(self))
        self.start_Search_2.clicked.connect(lambda: Sort(self))


        # -------------------- Customer Options ----------------------- #
        self.home_Btn.clicked.connect(lambda: self.changing_customerStack_PageNo(0))
        self.customer_logout_Btn.clicked.connect(lambda: self.changing_mainStack_PageNo(0))
        self.explore_Btn.clicked.connect(lambda: showing_explore_menu(self))
        self.fvt_Btn.clicked.connect(lambda: showing_fvt_items(self))
        self.cart_Btn.clicked.connect(lambda: showing_cart_items(self))
        self.order_history_Btn.clicked.connect(lambda: showing_all_orders(self))
        self.credentials_Btn.clicked.connect(lambda: update_data(self))


    # ------------------- Changing Connections ------------------- #
    def checking_the_connection(self, btn_or_table):
        num_receivers = btn_or_table.receivers(btn_or_table.clicked)
        # less than and equal to zero means the button is not connected to any function
        if num_receivers > 0:
            btn_or_table.clicked.disconnect()
            return True
        else:
            return True


    # ---------------------- Getting Data ------------------------ #
    def get_whole_row(self, index, table):
        row = index.row()
        model = table.model()

        if model is not None:
            self.table_item = [model.index(row, column).data(Qt.DisplayRole) for column in range(model.columnCount(index))]


    # ---------------------- Message Boxes ------------------------ #
    def show_Warning(self, message):
        QMessageBox.warning(self, "Warning", message)

    def show_Information(self, message):
        QMessageBox.information(self, "Information", message)


    # ---------------------- Changing Page ------------------------ #
    def back_from_about(self):
        self.changing_mainStack_PageNo(self.about_pagerecord)

    def back_from_cart_interface(self):
        self.changing_customerStack_PageNo(self.back_from_cart)

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
        if index == 0:
            showing_first_page(self)
        elif index == 2:
            self.back_from_cart = self.customerStack.currentIndex()
        
        self.customerStack.setCurrentIndex(index)



    # -------------------- Load admin Tables -------------------- #
    def view_foods(self):
        self.adminTable.setModel(FoodTableModel(Menu._food_list, self.foods_columns))
        header = self.adminTable.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.changing_adminoption_stack_PageNo(0)

    def view_orders(self,ordlist,table):
        table.setModel(OrderTableModel(ordlist, self.orders_columns))
        header = table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

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
    