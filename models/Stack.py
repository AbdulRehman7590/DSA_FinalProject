# ------------------------- Node --------------------------------- #
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# ------------------------ Stack --------------------------------- #
class Stack:
    def __init__(self):
        self.top = None

    # ------------------------ Push ------------------------------ #
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    # ------------------------- Pop ------------------------------ #
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    # ------------------------ Top ------------------------------ #
    def top_element(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    # ----------------------- Empty? ---------------------------- #
    def is_empty(self):
        return self.top is None

    # ----------------------- Display ---------------------------- #
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            while current is not None:
                print(current.data, end="    ")
                current = current.next
            print()

