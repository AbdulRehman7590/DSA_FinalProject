class Node:
    def __init__(self, data):
        self.next = None
        self.previous = None
        self.data = data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head.previous = new_head
            self.head = new_head

        return self.head
    
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

    def display(self):
        print("Null->", end="")
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next

        print("Null")

# Main function
if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert(12)
    dll.insert(14)
    dll.display()
    dll.insert_at_head(10)
    dll.display()
    dll.insert_at_tail(16)
    dll.display()
    flag = dll.search(18)
    if flag:
        print("Key Found")
    else:
        print("Key Not Found")
