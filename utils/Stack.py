class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def top_element(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            while current is not None:
                print(current.data, end="    ")
                current = current.next
            print()

if __name__ == "__main__":
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:")
    stack.display()

    print("Top element:", stack.top_element())

    print("Popped element:", stack.pop())

    print("Stack after pop:")
    stack.display()
