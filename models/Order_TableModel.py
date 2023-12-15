#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant


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
            key = list(self._orderdata.keys())[index.row()]
            column = self._headers[index.column()]
            value = self._orderdata[key]
        
            if column == "Order ID":
                return value.order_id
            elif column == "Order Status":
                return value.order_status
            elif column == "Order Date":
                return value.order_date
            elif column == "Ordered Items":
                return value.ordered_items
            elif column == "Order Address":
                return value.order_address
            elif column == "Order Total Price":
                return value.order_total_price
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None