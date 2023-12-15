# ----------------------- Modules -------------------------------- #
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from classes.BL.order import Order
from classes.DL.menu import Menu
from classes.DL.usersDL import UsersDL as dL

# ------------------- Showing explore menu ------------------------- #
def showing_explore_menu(self):
    self.changing_customerStack_PageNo(1)
    self.explore_more_page.setLayout(add_foodtab_in_widget(self, Menu._food_list))


# ----------------- Adding food in fvt list ------------------------ #
def add_to_fvt(self, food):
    (dL.get_user(self.userName).data).add_to_wishlist(Menu._food_list.search_data(food.food_name))


# ----------------- Showing add to cart page ----------------------- #
def showing_add_to_cart(self, food):
    self.changing_customerStack_PageNo(2)

    photo = self.findChild(QLabel, "food_img_Lbl")
    pixmap = QPixmap(food.food_img_path)
    photo.setPixmap(pixmap)
    photo.setScaledContents(True)

    name = self.findChild(QLabel, "food_name_Lbl")
    name.setText(food.food_name)

    rating = self.findChild(QLabel, "food_rating_Lbl")
    if food.food_rating == 5:
        path = f"views/Icons & logos/5star.png"
    elif food.food_rating == 4:
        path = f"views/Icons & logos/4star.png"
    elif food.food_rating == 3:
        path = f"views/Icons & logos/3star.png"
    elif food.food_rating == 2:
        path = f"views/Icons & logos/2star.png"
    else:
        path = f"views/Icons & logos/1star.png"
    pixmap = QPixmap(path)
    rating.setPixmap(pixmap)
    rating.setScaledContents(True)

    desc = self.findChild(QLabel, "food_description_Lbl")
    desc.setText(food.food_description)

    price = self.findChild(QLabel, "food_price_Lbl")
    price.setText(f"{food.food_price}")

    no_of_items = self.findChild(QSpinBox, "items_no_for_order")
    no_of_items.valueChanged.connect(lambda: self.findChild(QLabel, "food_price_Lbl").setText(f"{int(food.food_price) * int(no_of_items.value())}"))

    self.backexplore_Btn.clicked.connect(lambda: self.changing_customerStack_PageNo(1))
    self.backexplore_Btn.clicked.connect(lambda: no_of_items.setValue(1))

    self.add_tofvt_Btn.clicked.connect(lambda: add_to_fvt(self, food))


# ---------------------- Food Tab ------------------------------- #
def food_tab(self, food):
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
    button1.setIcon(QtGui.QIcon("views/Icons & logos/touch_fvt.png"))
    button1.clicked.connect(lambda: add_to_fvt(self, food))

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
def add_foodtab_in_widget(self, _food_list):
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    content_widget = QWidget()
    scroll_area.setWidget(content_widget)

    grid_layout = QGridLayout(content_widget)

    row = 0
    col = 0
    for i in range(_food_list.get_items_count()):
        grid_layout.addWidget(food_tab(self, _food_list.get_item_at_index(i)), row, col)
        col += 1
        if col >= 3:
            col = 0
            row += 1

    layout = QVBoxLayout()
    layout.addWidget(scroll_area)

    return layout