# ------------------------ Imports ------------------------------ #
from models.Linkedlist import LinkedList
from utils.algorithms import *

# ------------------------ Queue --------------------------------- #
class Queue:
    def __init__(self):
        self._queue_list = LinkedList()

    # ----------------------- Enqueue ---------------------------- #
    def enqueue(self, value):
        self._queue_list.insert_at_tail(value)

    # ----------------------- Dequeue ---------------------------- #
    def dequeue(self):
        return self._queue_list.delete_from_head()

    # ----------------------- Front ---------------------------- #
    def front_element(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._queue_list.head.data

    # --------------- get item at index ------------------------- #
    def get_item_at(self, index):
        return self._queue_list.get_item_at_index(index)

    # ---------------------- Empty? --------------------------- #
    def is_empty(self):
        return self._queue_list.get_items_count() == 0
    
    # ----------------------- Size ---------------------------- #
    def size(self):
        return self._queue_list.get_items_count()

    # --------------------- Display --------------------------- #
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self._queue_list.display()
     # --------------------- Search --------------------------- #        
    def search_data_with_filter(self, columnName, search_key, filter):
        data = []
        
        if self.is_empty():
            return None
        else:
            temp = self._queue_list.head

            while temp is not None:
                current_data = temp.data

                column_value = getattr(current_data, columnName)

                if filter == 1 and search_key in column_value:
                    data.append(current_data)
                elif filter == 2 and column_value.startswith(search_key):
                    data.append(current_data)
                elif filter == 3 and column_value.endswith(search_key):
                    data.append(current_data)

                temp = temp.next

        return None if len(data) == 0 else data

