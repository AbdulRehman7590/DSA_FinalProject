# ----------------------- Modules ------------------------------ #
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Classes.DL.menu import Menu
from Classes.BL.foods import Food
from Classes.DL.usersDL import UsersDL as dL
from Classes.BL.Customers import Customer
from utils.searching_algo import LinearSearch
from models.Linkedlist import LinkedList
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import pydot
# ---------------------- Admin Options -------------------------- #
def upload_photo(self):

        path , _ = QFileDialog.getOpenFileName(self, "Upload food image", "","")
        self.food_img_path = path.split("/")[-1]
        print(self.food_img_path)

# --------------------- Add foodin list ------------------------- #
def add_new_food(self):

    food_name = self.findChild(QLineEdit, "food_name").text()
    food_price = self.findChild(QLineEdit, "food_price").text()
    food_description = self.findChild(QLineEdit, "food_description").text()
    
    image_path = f"views/Images/{self.food_img_path}"
    if food_name == "" or food_price == "" or food_description == "" or image_path == "":
        self.show_Warning("Please fill all the fields")

        
    else:
        food = Food(food_name, food_price, image_path, food_description, 0)
        if Menu.add_food(food):
            self.show_Information("Food Added Successfully")
        else:
            self.show_Warning("Food already exists")
        self.view_foods()
        
        Menu.store_in_csv()


# ---------------------- Remove food ---------------------------- #
def remove_food(self):
    if self.table_item != "" and Menu._food_list.search_data(self.table_item[0]):
        item = Menu._food_list.search_data(self.table_item[0])
        self.table_item = ""
        
        Menu._food_list.delete_node(item)
        self.show_Information("Food removed successfully.")
        Menu.store_in_csv()
    else:
        self.show_Warning("Please select a food to remove")


# ---------------------- Searching food ------------------------- #
def search_food(self):
    column = self.searching_attribute.currentText().lower()
    filte = self.search_filter.currentIndex()
    search_key = self.search_content.text()

    if search_key == "":
        self.show_Warning("Please enter a key to search")
    else:
        data = LinearSearch(Menu._food_list, column, search_key, filte)
        dummy = LinkedList()
        for item in data:
            dummy.insert_at_tail(item)
        self.view_foods(dummy)




# ---------------------- Sorting food --------------------------- #
def sorting_foods(self):
    sorting_attribute = self.findChild(QComboBox, "sorting_attribute").currentText().lower()
    sorting_order = self.findChild(QComboBox, "sorting_order").currentIndex()
    if sorting_order == 0:
        Menu._food_list.sort(sorting_attribute, True)
    else:
        Menu._food_list.sort(sorting_attribute, False)

# --------------------- View order list ------------------------- #
def view_orders_for_admin(self):
    self.changing_adminoption_stack_PageNo(1)
    self.view_orders(None, self.adminTable)
    
    self.order_complete_Btn.hide()
    
    if self.checking_the_connection(self.view_pending_Btn):
        self.view_pending_Btn.clicked.connect(lambda: self.view_orders(self.user.pending_orders, self.adminTable))
        self.view_pending_Btn.clicked.connect(lambda: self.order_complete_Btn.show())
    
    if self.checking_the_connection(self.order_complete_Btn):
        self.order_complete_Btn.clicked.connect(lambda: complete_order(self))

    if self.checking_the_connection(self.view_delivered_Btn):
        self.view_delivered_Btn.clicked.connect(lambda: self.view_orders(self.user.delivered_orders, self.adminTable))

def complete_order(self):
    if self.user.pending_orders.size() > 0:
        self.user.add_delivered_order()
        self.show_Information("1st Order Completed")
    else:
        self.show_Warning("No orders received")


# --------------------- View food stats ------------------------- #
def showing_stats(self):
    self.changing_adminStack_PageNo(2)

    Layout = self.findChild(QHBoxLayout, "stats_layout")

    if Layout.count() > 0:
        for i in reversed(range(Layout.count())):
            Layout.itemAt(i).widget().setParent(None)

    self.figure = plt.figure(figsize=(15, 5))
    self.canvas = FigureCanvas(self.figure)
    Layout.addWidget(self.canvas)

    self.figure.clear()

    self.ax = self.figure.add_subplot(111)
    self.ax.set_title("Food Rating Stats")
    self.ax.set_ylabel("Food Rating")
    self.ax.grid(True)
    self.ax.set_ylim(0, 5)
    self.ax.set_yticks([0,1,2,3,4,5])
    self.ax.set_yticklabels([0,1,2,3,4,5])
    self.ax.spines['top'].set_visible(True)
    self.ax.spines['right'].set_visible(True)
    self.ax.spines['bottom'].set_visible(True)
    self.ax.spines['left'].set_visible(True)


    foods = Menu._food_list.head
    food_names = []
    food_ratings = []
    while foods is not None:
        food_names.append(foods.data.food_name.split(' ')[-1])
        food_ratings.append(foods.data.food_rating)
        foods = foods.next

    self.ax.bar(food_names, food_ratings, color="green")
    self.ax.set_xticks(range(len(food_names)))
    self.ax.set_xticklabels(food_names, rotation=90, ha="right", va="top")
    self.canvas.draw()


# --------------------- View users list ------------------------- #
def view_users_for_admin(self):
    self.view_customers()
    
    if self.checking_the_connection(self.remove_user_Btn):
        self.remove_user_Btn.clicked.connect(lambda: remove_user(self))

    if self.checking_the_connection(self.view_graph_Btn):
        self.view_graph_Btn.clicked.connect(lambda: visualize_bst(dL._user_list.root))

def remove_user(self):
    if self.table_item != "" and dL._user_list.findNode(self.table_item[0]):
        item = dL._user_list.findNode(self.table_item[0])
        self.table_item = ""
        if type(item) == Customer:
            dL._user_list.deleteNode(item)
            self.show_Information("User removed successfully.")
            dL.store_in_csv()
        else:
            self.show_Warning("You can't remove admin")
    else:
        self.show_Warning("Please select a user to remove")


# ----------------------- Visualize BST ------------------------- #
def visualize_bst(root, clear_previous=True):
    if clear_previous:
        plt.clf()

    edges = []
    traverse_tree(root, edges)

    graph = pydot.Dot(graph_type='graph')
    for edge in edges:
        graph.add_edge(pydot.Edge(str(edge[0]), str(edge[1])))

    node_style = {'fillcolor': 'yellow', 'style': 'filled'}
    
    for node in graph.get_nodes():
        node.set(**node_style)

    graph.set_graph_defaults(rankdir='TB')

    plt.title("Binary Search Tree")
    plt.axis('off')

    graph.write_png('bst_graph.png')
    plt.imshow(plt.imread('bst_graph.png'))
    plt.show()


def traverse_tree(node, edges):
    if node.left:
        edges.append((node.data.username, node.left.data.username))
        traverse_tree(node.left, edges)
    if node.right:
        edges.append((node.data.username, node.right.data.username))
        traverse_tree(node.right, edges)
