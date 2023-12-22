# ----------------------- Modules -------------------------------- #
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random as rnd
from datetime import date

from classes.BL.order import Order
from classes.DL.menu import Menu
from classes.DL.usersDL import UsersDL as dL
from utils.searching_algo import LinearSearch
from models.Linkedlist import LinkedList


# -------------------- Showing first page -------------------------- #
def showing_first_page(self):
    top_items = self.findChild(QWidget, "top_items_wdgt")
    if top_items.layout() is None:
        top_items.setLayout(add_foodtab_for_first_page(self, Menu._food_list, True))
    
    best_sell_items = self.findChild(QWidget, "best_sell_items_wdgt")
    if best_sell_items.layout() is None:
        best_sell_items.setLayout(add_foodtab_for_first_page(self, Menu._food_list, False))


# ------------------- Showing explore menu ------------------------- #
def showing_explore_menu(self):
    self.changing_customerStack_PageNo(1)

    Layout = self.findChild(QHBoxLayout, "explore_layout")
    if Layout.count() > 0:
        for i in reversed(range(Layout.count())):
            Layout.itemAt(i).widget().setParent(None)
    add_foodtab_in_widget(self, Layout, Menu._food_list, True)

    if self.checking_the_connection(self.explore_search_Btn):
        self.explore_search_Btn.clicked.connect(lambda: searching_food(self, Layout))

def searching_food(self, layout):
    search_key = self.explore_search_Line.text()

    if search_key == "":
        self.show_Warning("Please enter a key to search")
    else:
        data = LinearSearch(Menu._food_list, "food_name", search_key, 1)
        dummy = LinkedList()
        for item in data:
            dummy.insert_at_tail(item)
        
        if layout.count() > 0:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().setParent(None)
        add_foodtab_in_widget(self, layout, dummy, True)


# ------------------ Showing fvt items list ------------------------ #
def showing_fvt_items(self):
    self.changing_customerStack_PageNo(3)

    if self.user.wishlist.size() == 0:
        self.show_Warning("No items in wishlist")
    else:
        Layout = self.findChild(QHBoxLayout, "fvt_items_layout")
        if Layout.count() > 0:
            for i in reversed(range(Layout.count())):
                Layout.itemAt(i).widget().setParent(None)
        add_foodtab_in_widget(self, Layout, self.user.wishlist, False)


# ----------------- Showing add to cart page ----------------------- #
def showing_add_to_cart(self, food):
    self.changing_customerStack_PageNo(2)

    photo = self.findChild(QLabel, "food_img_Lbl")
    photo.setPixmap(QtGui.QPixmap(food.food_img_path))
    photo.setScaledContents(True)

    name = self.findChild(QLabel, "food_name_Lbl")
    name.setText(food.food_name)

    rate_wdgt = self.findChild(QWidget, "food_rating_wdgt")
    if rate_wdgt.layout() is None:
        layout = QHBoxLayout()
        rate_wdgt.setLayout(layout)
    
    for i in range(int(food.food_rating)):
        rate_wdgt.layout().addWidget(QLabel(), 0, Qt.AlignLeft)
        rate_wdgt.layout().itemAt(i).widget().setPixmap(QtGui.QPixmap("views/Icons & logos/star.png"))
        rate_wdgt.layout().itemAt(i).widget().setScaledContents(True)
        rate_wdgt.layout().itemAt(i).widget().setFixedHeight(20)
        rate_wdgt.layout().itemAt(i).widget().setFixedWidth(20)
    
    desc = self.findChild(QLabel, "food_description_Lbl")
    desc.setText(food.food_description)
    desc.setWordWrap(True)

    price = self.findChild(QLabel, "food_price_Lbl")
    price.setText(f"{food.food_price}")

    no_of_items = self.findChild(QSpinBox, "items_no_for_order")
    no_of_items.setValue(1)
    no_of_items.valueChanged.connect(lambda: price.setText(f"{int(food.food_price) * int(no_of_items.value())}"))
    
    if self.checking_the_connection(self.backexplore_Btn):
        self.backexplore_Btn.clicked.connect(self.back_from_cart_interface)
    
    if self.checking_the_connection(self.add_tofvt_Btn):
        self.add_tofvt_Btn.clicked.connect(lambda: add_to_fvt(self, food))

    if self.checking_the_connection(self.add_tocart_Btn):
        self.add_tocart_Btn.clicked.connect(lambda: add_to_cart(self, food, int(no_of_items.value())))


# ------------------- Showing cart items --------------------------- #
def showing_cart_items(self):
    self.changing_customerStack_PageNo(4)
    self.view_orders(self.user.cart, self.customer_table)
    
    if self.checking_the_connection(self.customer_table):
        self.customer_table.clicked.connect(lambda: self.get_whole_row(self.customer_table.currentIndex(), self.customer_table))
    
    if self.checking_the_connection(self.remove_cart_Btn):
        self.remove_cart_Btn.clicked.connect(lambda: check_item(self))

    if self.checking_the_connection(self.buy_items_Btn):
        self.buy_items_Btn.clicked.connect(lambda: buy_all_items(self))

def check_item(self):
    if self.table_item == "":
        self.show_Warning("Please select an item first")
    else:
        item = self.user.cart.get_item_at_index(self.table_item[0])
        self.table_item = ""
        
        self.user.remove_from_cart(item)
        self.show_Information("Item removed from cart successfully.")

def buy_all_items(self):
    key = self.user.cart.keys()
    if len(key) > 0:
        for i in range(len(key)):
            ord = self.user.cart.get_item_at_index(key[i])
            self.user.add_to_ordered_items_list(ord)
            admin = dL.get_user("admin")
            admin.add_order(ord)
        self.show_Information("Items bought successfully. Check the order history section")
    else:
        self.show_Warning("Please add items in cart first")


# ------------------- Showing order history ------------------------ #
def showing_all_orders(self):
    self.changing_customerStack_PageNo(5)
    self.show_Information("Click on any button below and select any order to view details")

    if self.checking_the_connection(self.all_orders_Btn):
        self.all_orders_Btn.clicked.connect(lambda: self.view_orders(self.user.ordered_items_list, self.customer_table_2))
    
    if self.checking_the_connection(self.delivered_Items_Btn):
        self.delivered_Items_Btn.clicked.connect(lambda: self.view_orders(self.user.delivered_order_list, self.customer_table_2))

    if self.checking_the_connection(self.customer_table_2):
        self.customer_table_2.clicked.connect(lambda: self.get_whole_row(self.customer_table_2.currentIndex(), self.customer_table_2))
        self.customer_table_2.clicked.connect(lambda: showing_item(self, Menu._food_list.search_data(self.table_item[4])))

def showing_item(self, item):
    self.order_item_Lbl.setText(item.food_name)
    self.order_item_spec_Lbl.setText(item.food_description)
    self.like_Btn.setEnabled(True)

    if self.checking_the_connection(self.like_Btn):
        self.like_Btn.clicked.connect(lambda: handle_like_button(self, item))

def handle_like_button(self, item):
    if self.like_bton == 0:
        item.add_like_and_rate()
        self.like_bton = 1  
        self.like_Btn.setIcon(QtGui.QIcon("views/Icons & logos/fill_like.png"))
    else:
        item.remove_like_and_rate()
        self.like_bton = 0
        self.like_Btn.setIcon(QtGui.QIcon("views/Icons & logos/like.png"))
    Menu.store_in_csv()


# ----------------- Adding food in fvt list ----------------------- #
def add_to_fvt(self, food):
    if self.user.add_to_wishlist(Menu._food_list.search_data(food.food_name)):
        self.show_Information("Item added to wishlist successfully")
    else:
        self.show_Warning("Item already in wishlist")


# ----------------- Removing food in fvt list --------------------- #
def remove_from_fvt(self, food):
    if self.user.remove_from_wishlist(food):
        self.show_Information("Item removed from wishlist successfully.")
        showing_fvt_items(self)
    else:
        self.show_Warning("Item not in wishlist")


# ------------------ Adding food in cart -------------------------- #
def add_to_cart(self, food, no_of_items):
    if self.user.add_to_cart(order(self.user, str(rnd.randint(1, 999)), date.today().strftime("%d/%m/%Y"), self.user.address, food, no_of_items, int(food.food_price) * no_of_items)):
        self.show_Information("Item added to cart successfully")
    else:
        self.show_Warning("Item already in cart")


# ------------------- Updating data ------------------------------- #
def update_data(self):
    self.changing_customerStack_PageNo(6)

    old_name = self.findChild(QLabel, "old_name_Lbl")
    old_name.setText(self.user.username)

    old_email = self.findChild(QLabel, "old_mail_Lbl")
    old_email.setText(self.user.email)

    old_password = self.findChild(QLabel, "old_password_Lbl")
    old_password.setText(self.user.password)

    old_address = self.findChild(QLabel, "old_address_Lbl")
    old_address.setText(self.user.address)

    if self.checking_the_connection(self.change_name_Btn):
        self.change_name_Btn.clicked.connect(lambda: change_name(self))

    if self.checking_the_connection(self.change_mail_Btn):
        self.change_mail_Btn.clicked.connect(lambda: change_email(self))

    if self.checking_the_connection(self.change_password_Btn):
        self.change_password_Btn.clicked.connect(lambda: change_password(self))

    if self.checking_the_connection(self.change_address_Btn):
        self.change_address_Btn.clicked.connect(lambda: change_address(self))

def change_name(self):
    new_name = self.findChild(QLineEdit, "change_name_Line")
    if new_name.text() == "":
        self.show_Warning("Please enter a valid name")
    else:
        self.user.username = new_name.text()
        self.show_Information("Name updated successfully")
        dL.store_in_csv()

def change_email(self):
    new_email = self.findChild(QLineEdit, "change_mail_Line")
    if new_email.text() == "":
        self.show_Warning("Please enter a valid email")
    else:
        self.user.email = new_email.text()
        self.show_Information("Email updated successfully")
        dL.store_in_csv()

def change_password(self):
    new_password = self.findChild(QLineEdit, "change_password_Line")
    if new_password.text() == "":
        self.show_Warning("Please enter a valid password")
    else:
        self.user.password = new_password.text()
        self.show_Information("Password updated successfully")
        dL.store_in_csv()

def change_address(self):
    new_address = self.findChild(QLineEdit, "change_address_Line")
    if new_address.text() == "":
        self.show_Warning("Please enter a valid address")
    else:
        self.user.address = new_address.text()
        self.show_Information("Address updated successfully")
        dL.store_in_csv()


# ------------------------ Food Tab ------------------------------- #
def food_tab(self, food, menu_flag):
    main_widget = QWidget()
    main_layout = QVBoxLayout()

    label = QLabel()
    label.setPixmap(QtGui.QPixmap(food.food_img_path))
    label.setScaledContents(True)
    label.setMinimumHeight(175)
    main_layout.addWidget(label)

    inner_widget = QGroupBox()
    inner_layout = QGridLayout()

    label1 = QLabel(f"{food.food_name}")
    label1.setStyleSheet(
        """
        QLabel {
            font-size: 18px;
            font: Rockwell;
            font-weight: bold;
            color: rgb(244,244,244);
        }
        """
    )
    label1.setWordWrap(True)
    label1.alignment = Qt.AlignCenter

    label2 = QLabel(f"Rs. {food.food_price}")
    label2.setStyleSheet(
        """
        QLabel {
            font-size: 14px;
            font: Rockwell;
            color: rgb(244,244,244);
        }
        """
    )
    label2.setWordWrap(True)
    label2.alignment = Qt.AlignCenter
    
    button1 = QPushButton()
    button1.setMinimumHeight(30)
    button1.setFixedWidth(135)
    button1.setStyleSheet(
                """
                QPushButton {
	                background-color:rgb(244,244,244);
	                border-radius:10%;

                }
                QPushButton:hover {
                    background-color: rgb(255, 91, 82);
                }
                """
    )
    if menu_flag:
        button1.setIcon(QtGui.QIcon("views/Icons & logos/touch_fvt.png"))
        if self.checking_the_connection(button1):
            button1.clicked.connect(lambda: add_to_fvt(self, food))
    else:
        button1.setIcon(QtGui.QIcon("views/Icons & logos/remove.png"))
        if self.checking_the_connection(button1):
            button1.clicked.connect(lambda: remove_from_fvt(self, food))

    button2 = QPushButton()
    button2.setMinimumHeight(30)
    button2.setFixedWidth(135)
    button2.setStyleSheet(
                """
                QPushButton {
	                background-color:rgb(244,244,244);
	                border-radius:10%;

                }
                QPushButton:hover {
                    background-color: rgb(255, 91, 82);
                }
                """
    )
    button2.setIcon(QtGui.QIcon("views/Icons & logos/add_cart.png"))
    if self.checking_the_connection(button2):
        button2.clicked.connect(lambda: showing_add_to_cart(self, food))

    inner_layout.addWidget(label1, 0, 0)
    inner_layout.addWidget(label2, 0, 1)
    inner_layout.addWidget(button1, 1, 0)
    inner_layout.addWidget(button2, 1, 1)
    inner_layout.setContentsMargins(2, 2, 2, 2)

    inner_widget.setLayout(inner_layout)
    inner_widget.setStyleSheet(
        """
        QGroupBox {
            border: 1px solid rgb(244,244,244);
        }
        """
    )
    
    main_layout.addWidget(inner_widget)
    
    main_widget.setLayout(main_layout)
    main_widget.setFixedHeight(300)
    main_widget.setFixedWidth(300)
    main_widget.setStyleSheet(
        """
        QWidget {
            background-color: rgba(230, 0, 35, 1);
            margin: 2px;
            border-radius: 10%;
        }
        """
    )
    
    return main_widget


# ------------------- Adding tab in widget ------------------------ #
def add_foodtab_in_widget(self, layout, food_list, menu_flag):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    content_widget = QWidget()
    scroll_area.setWidget(content_widget)

    
    grid_layout = QGridLayout(content_widget)

    row = 0
    col = 0
    for i in range(food_list.size()):
        grid_layout.addWidget(food_tab(self, food_list.get_item_at_index(i), menu_flag), row, col)
        col += 1
        if col >= 3:
            col = 0
            row += 1
    layout.addWidget(scroll_area)


# ------------------- Food tab for 1st page ----------------------- #
def food_tab_for_first_page(self, food):
    main_widget = QWidget()
    main_layout = QVBoxLayout()

    label = QLabel()
    label.setPixmap(QtGui.QPixmap(food.food_img_path))
    label.setScaledContents(True)
    label.setMinimumHeight(105)
    label.setStyleSheet(
        """
        QLabel {
            border-bottom-right-radius: 10%;
            border-bottom-left-radius: 10%;
        }
        """
    )
    main_layout.addWidget(label)

    button2 = QPushButton()
    button2.setMinimumHeight(30)
    button2.setFixedWidth(153)
    button2.setStyleSheet(
                """
                QPushButton {
	                background-color:rgb(244,244,244);
	                border-top-right-radius: 10%;
                    border-top-left-radius: 10%;
                }
                QPushButton:hover {
                    background-color: rgb(255, 91, 82);
                }
                """
    )
    button2.setIcon(QtGui.QIcon("views/Icons & logos/add_cart.png"))
    if self.checking_the_connection(button2):
        button2.clicked.connect(lambda: showing_add_to_cart(self, food))

    main_layout.addWidget(button2)
    
    main_widget.setLayout(main_layout)
    main_widget.setFixedHeight(147)
    main_widget.setFixedWidth(170)
    main_widget.setStyleSheet(
        """
        QWidget {
            background-color: rgba(230, 0, 35, 1);
            margin: 2px;
            border-radius: 10%;
        }
        """
    )
    
    return main_widget


# ------------------- Adding tab in widget ------------------------ #
def add_foodtab_for_first_page(self, food_list, top_flag):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)

    content_widget = QWidget()
    scroll_area.setWidget(content_widget)

    horizontal_layout = QHBoxLayout(content_widget)

    count = 0
    for i in range(food_list.size()):
        if int(top_flag and food_list.get_item_at_index(i).food_rating) >= 4 and count < 10:
            horizontal_layout.addWidget(food_tab_for_first_page(self, food_list.get_item_at_index(i)))
            count += 1
        elif int(food_list.get_item_at_index(i).food_likes) >= 4 and count < 10:
            horizontal_layout.addWidget(food_tab_for_first_page(self, food_list.get_item_at_index(i)))
            count += 1

    horizontal_layout.setContentsMargins(5, 0, 5, 0)
    horizontal_layout.setSpacing(5)
    
    layout = QHBoxLayout()
    layout.addWidget(scroll_area)

    return layout