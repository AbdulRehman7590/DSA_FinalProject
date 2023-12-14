# ------------------------ Food CLass ------------------------------ #
class Order():
    def __init__(self,order_id,order_status,order_date,ordered_items,order_address,order_total_price):
        self.__order_id = order_id
        self.__order_status = order_status
        self.__order_date = order_date
        self.__ordered_items = ordered_items
        self.__order_address = order_address
        self.__order_total_price = order_total_price

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
    def ordered_items(self)->str:
        return self.__ordered_items
    
    @property
    def order_address(self)->str:
        return self.__order_address
    
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

    @ordered_items.setter
    def ordered_items(self,ordered_items:str)->None:
        self.__ordered_items = ordered_items

    @order_address.setter
    def order_address(self,order_address:str)->None:
        self.__order_address = order_address

    @order_total_price.setter
    def order_total_price(self,order_total_price:str)->None:
        self.__order_total_price = order_total_price



