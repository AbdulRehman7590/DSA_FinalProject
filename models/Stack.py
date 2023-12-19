# ------------------------- Imports --------------------------------- #
from models.Linkedlist import LinkedList

# ------------------------ Stack --------------------------------- #
class Stack:
    def __init__(self):
        self._stack_list = LinkedList()

    # ------------------------ Push ------------------------------ #
    def push(self, value):
        self._stack_list.insert_at_head(value)

    # ------------------------- Pop ------------------------------ #
    def pop(self):
        return self._stack_list.delete_from_head()

    # ------------------------ Top ------------------------------ #
    def top_element(self):
        return self._stack_list.head.data

    # --------------- get item at index ------------------------- #
    def get_item_at(self, index):
        return self._stack_list.get_item_at_index(index)

    # ----------------------- Empty? ---------------------------- #
    def is_empty(self):
        return self._stack_list.size() == 0

    # ----------------------- Size ---------------------------- #
    def size(self):
        return self._stack_list.size()

    # ----------------------- Display ---------------------------- #
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            self._stack_list.display()

