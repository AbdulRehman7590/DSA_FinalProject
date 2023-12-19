# ------------------------ Imports ------------------------------ #
from models.Linkedlist import LinkedList

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
        return self._queue_list.size() == 0
    
    # ----------------------- Size ---------------------------- #
    def size(self):
        return self._queue_list.size()

    # --------------------- Display --------------------------- #
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self._queue_list.display()

