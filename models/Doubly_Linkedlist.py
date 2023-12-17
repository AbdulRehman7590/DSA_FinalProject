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
            self.tail = new_tail
            

    # ------------------- Deleting node ------------------------- #
    def delete_data(self, data):
        if self.head is None:
            return False
        else:
            if self.head.data == data:
                self.head.previous = None
                self.head = self.head.next
                return True
            else:
                temp = self.head
                while temp.next is not None:
                    if temp.data == data:
                        temp.next.previous = temp.previous
                        temp.previous.next = temp.next
                        return True
                    else:
                        temp = temp.next
            return False

    # ----------------------- Search ---------------------------- #
    def search_data(self, foodname):
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data.food_name == foodname:
                    return temp.data
                else:
                    temp = temp.next
        return None
    
    # ------------------- Get item at Index  --------------------- #
    def get_item_at_index(self, index):
        idx = 0
        if self.head is None:
            return None
        else:
            temp = self.head
            while temp is not None:
                if idx == index:
                    return temp.data
                else:
                    temp = temp.next
                    idx += 1
        return None
    
    # --------------------- Get items count ---------------------- #
    def get_items_count(self):
        count = 0
        if self.head is None:
            return count
        else:
            temp = self.head
            while temp is not None:
                count += 1
                temp = temp.next
        return count
    
    # ----------------------- Display ---------------------------- #
    def display(self):
        print("Null->", end="")
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Null")

