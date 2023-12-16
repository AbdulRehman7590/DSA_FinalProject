# ----------------------- Modules -------------------------------- #
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random as rnd
from datetime import date

import random as rnd
from datetime import date

from classes.BL.order import Order
from classes.DL.menu import Menu


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

    if self.explore_more_page.layout() is not None:
        for i in reversed(range(self.explore_more_page.layout().count())): 
            self.explore_more_page.layout().itemAt(i).widget().setParent(None)
    self.explore_more_page.setLayout(add_foodtab_in_widget(self, Menu._food_list, True))


# ------------------ Showing fvt items list ------------------------ #
def showing_fvt_items(self):
    self.changing_customerStack_PageNo(3)

    if self.cust_fvt_page.layout() is not None:
        for i in reversed(range(self.cust_fvt_page.layout().count())): 
            self.cust_fvt_page.layout().itemAt(i).widget().setParent(None)
    self.cust_fvt_page.setLayout(add_foodtab_in_widget(self, self.user.wishlist, False))


# ----------------- Showing add to cart page ----------------------- #
def showing_add_to_cart(self, food):
    self.changing_customerStack_PageNo(2)

    photo = self.findChild(QLabel, "food_img_Lbl")
    photo.setPixmap(QtGui.QPixmap(food.food_img_path))
    photo.setScaledContents(True)

    name = self.findChild(QLabel, "food_name_Lbl")
    name.setText(food.food_name)

    rate_wdgt = self.findChild(QWidget, "food_rating_wdgt")
    if rate_wdgt.layout() is not None:
        for i in reversed(range(rate_wdgt.layout().count())): 
            rate_wdgt.layout().itemAt(i).widget().setParent(None)
    else:
        layout = QHBoxLayout()
        rate_wdgt.setLayout(layout)
    
    for i in range(int(food.food_rating)):
        rate_wdgt.layout().addWidget(QLabel(), 0, Qt.AlignLeft)
        rate_wdgt.layout().itemAt(i).widget().setPixmap(QtGui.QPixmap("views/Icons & logos/fill_star.png"))
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
    no_of_items.valueChanged.connect(lambda: self.findChild(QLabel, "food_price_Lbl").setText(f"{int(food.food_price) * int(no_of_items.value())}"))
    
    self.backexplore_Btn.clicked.connect(self.back_from_cart_interface)

    self.add_tofvt_Btn_lambda = lambda: add_to_fvt(self, food)
    self.add_tofvt_Btn.clicked.connect(self.add_tofvt_Btn_lambda)

    self.add_tocart_Btn_lambda = lambda: add_to_cart(self, food, int(no_of_items.value()))
    self.add_tocart_Btn.clicked.connect(self.add_tocart_Btn_lambda)


# ------------------- Showing cart items --------------------------- #
def showing_cart_items(self):
    self.changing_customerStack_PageNo(4)
    self.view_orders(self.user.cart, self.customer_table)
    
    self.customer_table.clicked.connect(lambda: get_whole_row(self, self.customer_table.currentIndex(), self.customer_table))
    
    self.remove_cart_Btn.clicked.connect(lambda: check_item(self, False))
    self.buy_items_Btn.clicked.connect(lambda: check_item(self, True))

def check_item(self, flag):
    if self.cart_item == "":
        self.show_Warning("Please select an item first")
    else:
        item = self.user.cart.search(self.cart_item[0])
        self.cart_item = ""
        if flag:
            self.user.add_to_ordered_items_list(item)
            self.show_Information("Item bought successfully.")
        else:
            self.user.remove_from_cart(item)
            self.show_Information("Item removed from cart successfully.")


def get_whole_row(self, index, table):
    row = index.row()
    model = table.model()

    if model is not None:
        self.cart_item = [model.index(row, column).data(Qt.DisplayRole) for column in range(model.columnCount(index))]

# ------------------- Showing order history ------------------------ #
def showing_all_orders(self):
    self.changing_customerStack_PageNo(5)
    self.show_Information("Click on any button below and select any order to view details")

    self.all_orders_Btn.clicked.connect(lambda: self.view_orders(self.user.ordered_items_list, self.customer_table_2))
    self.delivered_Items_Btn.clicked.connect(lambda: self.view_orders(self.user.delivered_order_list, self.customer_table_2))

    self.customer_table_2.clicked.connect(lambda: get_whole_row(self.customer_table_2.currentIndex(), self.customer_table_2))
    self.customer_table_2.clicked.connect(lambda: showing_item(Menu._food_list.search_data(self.cart_item[3])))

def showing_item(self, item):
    self.order_item_Lbl.setText(item.food_name)
    self.order_item_spec_Lbl.setText(item.food_description)
    self.like_Btn.setEnabled(True)

    self.like_Btn.clicked.connect(lambda: self.handle_like_button(item))

def handle_like_button(self, item):
    if self.like_Btn.icon() == QtGui.QIcon("views/Icons & logos/like.png"):
        item.add_like_and_rate()  
        self.like_Btn.setIcon(QtGui.QIcon("views/Icons & logos/fill_like.png"))
    else:
        item.remove_like_and_rate()
        self.like_Btn.setIcon(QtGui.QIcon("views/Icons & logos/like.png"))


# ----------------- Adding food in fvt list ------------------------ #
def add_to_fvt(self, food):
    if self.user.add_to_wishlist(Menu._food_list.search_data(food.food_name)):
        self.show_Information("Item added to wishlist successfully")
    else:
        self.show_Warning("Item already in wishlist")


# ----------------- Removing food in fvt list ---------------------- #
def remove_from_fvt(self, food):
    if self.user.remove_from_wishlist(food):
        self.show_Information("Item removed from wishlist successfully")
    else:
        self.show_Warning("Item not in wishlist")


# ------------------ Adding food in cart --------------------------- #
def add_to_cart(self, food, no_of_items):
    if self.user.add_to_cart(Order(str(rnd.randint(1, 999)), date.today().strftime("%d/%m/%Y"), self.user.address, food, no_of_items, int(food.food_price) * no_of_items)):
        self.show_Information("Item added to cart successfully")
    else:
        self.show_Warning("Item already in cart")


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
        button1.clicked.connect(lambda: add_to_fvt(self, food))
    else:
        button1.setIcon(QtGui.QIcon("views/Icons & logos/remove.png"))
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
def add_foodtab_in_widget(self, food_list, menu_flag):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    content_widget = QWidget()
    scroll_area.setWidget(content_widget)

    
    grid_layout = QGridLayout(content_widget)

    row = 0
    col = 0
    for i in range(food_list.get_items_count()):
        grid_layout.addWidget(food_tab(self, food_list.get_item_at_index(i), menu_flag), row, col)
        col += 1
        if col >= 3:
            col = 0
            row += 1

    layout = QVBoxLayout()
    layout.addWidget(scroll_area)

    return layout


# ------------------- Food tab for 1st page ----------------------- #
def food_tab_for_first_page(self, food):
    main_widget = QWidget()
    main_layout = QVBoxLayout()

    label = QLabel()
    label.setPixmap(QtGui.QPixmap(food.food_img_path))
    label.setScaledContents(True)
    label.setMinimumHeight(115)
    main_layout.addWidget(label)

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
    button2.clicked.connect(lambda: showing_add_to_cart(self, food))

    main_layout.addWidget(button2)
    
    main_widget.setLayout(main_layout)
    main_widget.setFixedHeight(160)
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
    for i in range(food_list.get_items_count()):
        if int(top_flag and food_list.get_item_at_index(i).food_rating) >= 4 and count < 10:
            horizontal_layout.addWidget(food_tab_for_first_page(self, food_list.get_item_at_index(i)))
            count += 1
        elif int(food_list.get_item_at_index(i).food_likes) >= 4 and count < 10:
            horizontal_layout.addWidget(food_tab_for_first_page(self, food_list.get_item_at_index(i)))
            count += 1

    horizontal_layout.setContentsMargins(5, 2, 5, 2)
    horizontal_layout.setSpacing(5)
    
    layout = QHBoxLayout()
    layout.addWidget(scroll_area)

    return layout