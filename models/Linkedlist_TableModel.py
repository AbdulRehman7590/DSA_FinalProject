#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant


# ------------------ Dataframe into Model ----------------------- #
class LinkedListModel(QAbstractTableModel):
    def __init__(self, head=None, column_names=None, parent=None):
        super().__init__(parent)
        self.head = head
        self.column_names = column_names if column_names else ['Data']

    def rowCount(self, parent=None):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def columnCount(self, parent=None):
        return len(self.column_names)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            row = index.row()
            column = index.column()
            node = self.get_node_at_index(row)
            if node:
                if column == 0:
                    return str(node.data)
                

        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            if section < len(self.column_names):
                return self.column_names[section]
        return None

    def get_node_at_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        return None