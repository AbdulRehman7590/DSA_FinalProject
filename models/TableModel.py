from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QTableView, QWidget, QVBoxLayout
import sys

class CustomTableModel(QAbstractTableModel):
    def __init__(self, data, headers, parent=None):
        super().__init__(parent)
        self._data = data
        self._headers = headers

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self._data)):
            return QVariant()

        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            if col == 0:
                return self._data[row]['Name']
            elif col == 1:
                return str(self._data[row]['Price'])
        elif role == Qt.DecorationRole and col == 2:  # Assuming image path is in column 2
            image_path = self._data[row]['ImagePath']
            pixmap = QPixmap(image_path)
            scaled = pixmap.scaled(QSize(100, 100), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            return scaled

        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return QVariant()

