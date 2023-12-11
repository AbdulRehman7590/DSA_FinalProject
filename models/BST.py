class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, current, data):
        if current is None:
            return Node(data)

        elif data < current.data:
            current.left = self.insert(current.left, data)
        elif data > current.data:
            current.right = self.insert(current.right, data)
        else:
            print("No duplicates allowed")
        print("Entered in BST")
        return current
    
    

    def inorder(self, current):
        if not current:
            return
        self.inorder(current.left)
        print(current.data, end=" ")
        self.inorder(current.right)

    def preorder(self, current):
        if not current:
            return
        print(current.data, end=" ")
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self, current):
        if not current:
            return
        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data, end=" ")

    def insert_data(self, data):
        self.root = self.insert(self.root, data)

    def get_root(self):
        return self.root

    def search(self, root, key):
        if root is None or root.data == key:
            return root
        elif root.data > key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete_node(self, current, data):
        if current is None:
            return current

        if data < current.data:
            current.left = self.delete_node(current.left, data)
        elif data > current.data:
            current.right = self.delete_node(current.right, data)
        else:
            if current.left is None:
                temp = current.right
                del current
                return temp
            elif current.right is None:
                temp = current.left
                del current
                return temp

            temp = self.find_min(current.right)
            current.data = temp.data
            current.right = self.delete_node(current.right, temp.data)

        return current

    def delete_data(self, data):
        self.root = self.delete_node(self.root, data)

