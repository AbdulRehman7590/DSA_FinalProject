# ------------------------- Node --------------------------------- #
class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

# --------------------- Linked List ------------------------------ #
class DoubleLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    # ----------------------- Empty? ---------------------------- #
    def is_empty(self):
        return self.head is None

    # ------------------- Insert at Head ------------------------- #
    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head.previous = new_head
            self.head = new_head
        return self.head

    # ------------------- Insert at tail ------------------------- #
    def insert_at_tail(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            new_tail = Node(data)
            new_tail.previous = temp
            temp.next = new_tail
        return new_tail

    # ----------------------- Search ---------------------------- #
    def search(self, data):
        if self.head is None:
            return False
        else:
            temp = self.head
            while temp.next is not None:
                if temp.data == data:
                    return True
                else:
                    temp = temp.next
        return False

    # ----------------------- Display ---------------------------- #
    def display(self):
        print("Null->", end="")
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Null")

