#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant


# ------------------ stack into Model ----------------------- #
class StackTableModel(QAbstractTableModel):
    def __init__(self, stack, headers):
        super().__init__()
        self._stack = stack
        self._headers = headers

    def rowCount(self, index):
        return self._stack.size()

    def columnCount(self, index):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            key = list(self._stack.keys())[index.row()]
            column = self._headers[index.column()]
            value = self._stack[key]
        
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