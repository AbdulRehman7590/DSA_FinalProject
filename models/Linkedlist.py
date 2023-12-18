# ------------------------- Node --------------------------------- #
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

# --------------------- Linked List ------------------------------ #
class LinkedList: 
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
            self.head = new_head
        return self.head

    # ------------------- Insert at tail ------------------------- #
    def insert_at_tail(self, data):
        if self.head is None:
            obj = Node(data)
            self.head = obj
            self.tail = obj
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next

            new_tail = Node(data)
            temp.next = new_tail
            self.tail = new_tail
            
    # ------------------- Deleting node ------------------------- #
    def delete_node(self, data):
        if self.head is None:
            return None
        else:
            if self.head.data == data:
                return self.delete_from_head()
            else:
                temp = self.head
                while temp.next.data != data:
                    temp = temp.next
                temp.next = temp.next.next
                return temp.next.data

    # -------------------- Delete head -------------------------- #
    def delete_from_head(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    # -------------------- Delete Tail -------------------------- #
    def delete_from_tail(self):
        if self.head is None:
            return None
        else:
            if self.tail == self.head:
                return self.delete_from_head()
            else:
                temp = self.head
                while temp.next.data != self.tail.data:
                    temp = temp.next
                
                temp.next = self.tail.next
                self.tail = temp
                return self.tail.data

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

