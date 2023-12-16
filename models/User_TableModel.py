#----------------------- Imports ---------------------------------#
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from classes.BL.Customers import Customer

# -------------------- BST into Model -------------------------- #
class UserTableModel(QAbstractTableModel):
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
            user = self._tree.inOrderTraversal(self._tree.root, index.row())
            col = self._headers[index.column()]
            
            if user:
                if col == "Name":
                    return user.username
                elif col == "Email":
                    return user.email
                elif col == "Address":
                    return user.address
                elif col == "Type":
                    return "Customer" if type(user) == Customer else "Admin"
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return QVariant()