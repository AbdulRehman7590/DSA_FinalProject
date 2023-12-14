#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant


# ----------------- Linked list into Model ---------------------- #
class LinkedListTableModel(QAbstractTableModel):
    def __init__(self, linked_list, headers):
        super().__init__()
        self._linked_list = linked_list 
        self._headers = headers

    def rowCount(self, parent):
        return self._linked_list.get_items_count()

    def columnCount(self, parent):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = self._linked_list.get_item_at_index(index.row())
            col = self._headers[index.column()]
            
            if row is not None:
                if col == "Item_Name":
                    return row.food_name
                elif col == "Price":
                    return row.food_price
                elif col == "Description":
                    return row.food_description
                elif col == "Rating":
                    return row.food_rating
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None