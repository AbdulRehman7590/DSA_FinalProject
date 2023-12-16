# ------------------------- Modules -------------------------------- #
from models.Doubly_Linkedlist import DoubleLinkedList

# ------------------------ Food CLass ------------------------------ #
class Order():
    def __init__(self,order_id,order_date,order_address):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__order_address = order_address
        self.__ordered_items = DoubleLinkedList()
        self.__ordered_items_count = DoubleLinkedList()
        self.__order_total_price = 0

    # ------------------------ Getter ------------------------------ #
    @property
    def order_id(self)->str:
        return self.__order_id
    
    @property
    def order_status(self)->str:
        return self.__order_status
    
    @property
    def order_date(self)->str:
        return self.__order_date
    
    @property
    def order_address(self)->str:
        return self.__order_address
    
    @property
    def ordered_items(self)->str:
        return self.__ordered_items
    
    @property
    def ordered_items_count(self)->str:
        return self.__ordered_items_count
    
    @property
    def order_total_price(self)->str:
        return self.__order_total_price
    

    # ------------------------ Setter ------------------------------ #
    @order_id.setter
    def order_id(self,order_id:str)->None:
        self.__order_id = order_id

    @order_status.setter
    def order_status(self,order_status:str)->None:
        self.__order_status = order_status

    @order_date.setter
    def order_date(self,order_date:str)->None:
        self.__order_date = order_date

    @order_address.setter
    def order_address(self,order_address:str)->None:
        self.__order_address = order_address


    # ------------------------ Methods ------------------------------ #
    def add_ordered_items(self, item, count):
        self.__ordered_items.insert_at_tail(item)
        self.__ordered_items_count.insert_at_tail(count)
        self.__order_total_price += int(item.food_price) * count

