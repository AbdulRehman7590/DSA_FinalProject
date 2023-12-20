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
    def size(self):
        count = 0
        if self.head is None:
            return count
        else:
            temp = self.head
            while temp is not None:
                count += 1
                temp = temp.next
        return count
    
    # --------------------- Merge Sort Algo ---------------------- #
    def merge_sort(self, head, key, isAscending: bool = True):
        if not head or not head.next:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort(head, key, isAscending)
        right = self.merge_sort(next_to_middle, key, isAscending)

        sorted_list = self.merge(left, right, key, isAscending)
        return sorted_list

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right, key, isAscending: bool = True):
        dummy = Node(None)
        current = dummy

        while left and right:
            if isAscending:
                if getattr(left.data, int(key) if key != "food_name" else key) < getattr(right.data, int(key) if key != "food_name" else key):
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
            else:
                if getattr(left.data, int(key) if key != "food_name" else key) > getattr(right.data, int(key) if key != "food_name" else key):
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
            
            current = current.next

        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next

    def sort(self, key, isAscending: bool = True):
        self.head = self.merge_sort(self.head, key, isAscending)


    # ----------------------- Display ---------------------------- #
    def display(self):
        print("Null->", end="")
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Null")

