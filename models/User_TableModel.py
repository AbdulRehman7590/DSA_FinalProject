#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex


# -------------------- BST into Model -------------------------- #
class BSTTableModel(QAbstractTableModel):
    def __init__(self, tree, headers):
        super().__init__()
        self._tree = tree  
        self._headers = headers

    def rowCount(self, index):
        return self._tree.NumberOfNodes(self._tree.root) if self._tree.root else 0

    def columnCount(self, index):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            row = index.row()
            col = self._headers[index.column()]
            node = self._tree.findNode(row)
            if node:
                if col == "Username":
                    return node.data.username
                elif col == "Email":
                    return node.data.email
                elif col == "Password":
                    return node.data.password
                elif col == "Address":
                    return node.data.address
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return None