#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from models.Hash_Table import HashTable
from models.Stack import Stack
from models.Queue import Queue


# ------------------ orderdata into Model ---------------------- #
class OrderTableModel(QAbstractTableModel):
    def __init__(self, orderdata, headers):
        super().__init__()
        self._orderdata = orderdata
        self._headers = headers

    def rowCount(self, index):
        return self._orderdata.size()

    def columnCount(self, index):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            column = self._headers[index.column()]
            value = None
            if isinstance(self._orderdata, HashTable):
                key = self._orderdata.keys()[index.row()]
                value = self._orderdata.get_order(key)
            elif isinstance(self._orderdata, Stack):
                value = self._orderdata.top_element()
            elif isinstance(self._orderdata, Queue):
                value = self._orderdata.front_element()
            
            if value:
                if column == "Order_ID":
                    return value.order_id
                elif column == "Order_Date":
                    return value.order_date
                elif column == "Order_Address":
                    return value.order_address
                elif column == "Order_Item":
                    return value.ordered_items.food_name
                elif column == "Order_Quantity":
                    return value.ordered_items_count
                elif column == "Order_Total_Price":
                    return value.order_total_price
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return QVariant()