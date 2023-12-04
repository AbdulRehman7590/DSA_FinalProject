class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        dequeued_value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return dequeued_value

    def front_element(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current is not None:
                print(current.data, end=" <- ")
                current = current.next
            print("rear")

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue:")
    queue.display()

    print("Front element:", queue.front_element())

    print("Dequeued element:", queue.dequeue())

    print("Queue after dequeue:")
    queue.display()
 