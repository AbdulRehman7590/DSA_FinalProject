# ----------------------- Modules -------------------------------- #
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random as rnd
from datetime import date

from classes.BL.order import Order
from classes.DL.menu import Menu
from classes.DL.usersDL import UsersDL as dL



# ------------------- Showing explore menu ------------------------- #
def showing_explore_menu(self):
    self.changing_customerStack_PageNo(1)
    self.explore_more_page.setLayout(add_foodtab_in_widget(self, Menu._food_list, True))


# ------------------ Showing fvt items list ------------------------ #
def showing_fvt_items(self):
    self.changing_customerStack_PageNo(3)
    self.cust_fvt_page.setLayout(add_foodtab_in_widget(self, self.user.wishlist, False))


# ----------------- Showing add to cart page ----------------------- #
def showing_add_to_cart(self, food):
    self.changing_customerStack_PageNo(2)

    photo = self.findChild(QLabel, "food_img_Lbl")
    photo.setPixmap(QPixmap(food.food_img_path))
    photo.setScaledContents(True)

    name = self.findChild(QLabel, "food_name_Lbl")
    name.setText(food.food_name)

    rate_wdgt = self.findChild(QWidget, "food_rating_wdgt")
    layout = QHBoxLayout()
    rate_wdgt.setLayout(layout)
    for _ in range(int(food.food_rating)):
        label = QLabel()
        label.setFixedWidth(20)
        label.setFixedHeight(20)
        label.setPixmap(QPixmap("views/Icons & logos/star.png"))
        label.setScaledContents(True)
        layout.addWidget(label)
    
    desc = self.findChild(QLabel, "food_description_Lbl")
    desc.setText(food.food_description)
    desc.setWordWrap(True)

    price = self.findChild(QLabel, "food_price_Lbl")
    price.setText(f"{food.food_price}")

    no_of_items = self.findChild(QSpinBox, "items_no_for_order")
    no_of_items.valueChanged.connect(lambda: self.findChild(QLabel, "food_price_Lbl").setText(f"{int(food.food_price) * int(no_of_items.value())}"))

    self.backexplore_Btn.clicked.connect(self.back_from_cart_interface)
    self.backexplore_Btn.clicked.connect(lambda: no_of_items.setValue(1))

    self.add_tofvt_Btn.clicked.connect(lambda: add_to_fvt(self, food))

    self.add_tocart_Btn.clicked.connect(lambda: add_to_cart(self, food, int(no_of_items.value())))


# ------------------- Showing cart items --------------------------- #
def showing_cart_items(self):
    self.view_orders(self,self.user.cart, self.customer_table)

    self.remove_cart_Btn.clicked.connect(lambda: self.user.remove_from_cart(self.user.cart.search_data(self.customer_table.model().data(self.customer_table.currentIndex()))))
    self.view_order_Btn.clicked.connect(lambda: self.view_orders(self,(self.user.cart.search_data(self.customer_table.model().data(self.customer_table.currentIndex()))).ordered_items_list, self.customer_table))
    self.buy_items_Btn.clicked.connect(lambda: self.user.add_to_ordered_items_list(self.user.cart.search_data(self.customer_table.model().data(self.customer_table.currentIndex()))))


# ----------------- Adding food in fvt list ------------------------ #
def add_to_fvt(self, food):
    self.user.add_to_wishlist(Menu._food_list.search_data(food.food_name))


# ------------------ Adding food in cart --------------------------- #
def add_to_cart(self, food, no_of_items):
    order = Order(rnd.randint(1, 999), date.today(), self.user.address)
    order.add_ordered_items(food, no_of_items)
    self.user.add_to_cart(order)


# ------------------------ Food Tab ------------------------------- #
def food_tab(self, food, menu_flag):
    main_widget = QWidget()
    main_layout = QVBoxLayout()

    label = QLabel()
    pixmap = QPixmap(food.food_img_path)
    label.setPixmap(pixmap)
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
        button1.clicked.connect(lambda: self.user.remove_from_wishlist(food))

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


