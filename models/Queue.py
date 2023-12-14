# ------------------------- Node --------------------------------- #
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# ------------------------ Queue --------------------------------- #
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ----------------------- Enqueue ---------------------------- #
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    # ----------------------- Dequeue ---------------------------- #
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        dequeued_value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return dequeued_value

    # ----------------------- Front ---------------------------- #
    def front_element(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    # ---------------------- Empty? --------------------------- #
    def is_empty(self):
        return self.front is None
    
    # ----------------------- Size ---------------------------- #
    def size(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count

    # --------------------- Display --------------------------- #
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" <- ")
                current = current.next
            print("rear")

