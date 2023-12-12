import csv

class Node:
    def __init__(self, value, parentNode=None):
        self.data = value
        self.right = None
        self.left = None
        self.parent = parentNode

class BST:
    def __init__(self):
        self.root = None

    def insertNode(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            current = self.root
            parent = None
            while current is not None:
                parent = current
                if value.username < current.data.username:
                    current = current.left
                else:
                    current = current.right
            newNode.parent = parent
            if value.username < parent.data.username:
                parent.left = newNode
            else:
                parent.right = newNode
        return newNode

    def findNode(self, value):
        temp = self.root
        lastNode = None
        while temp is not None:
            if value < temp.data.username:
                lastNode = temp
                temp = temp.left
            elif value > temp.data.username:
                lastNode = temp
                temp = temp.right
            else:
                return temp
        return lastNode

    def NumberOfNodes(self, T):
        if T is None:
            return 0
        return 1 + self.NumberOfNodes(T.left) + self.NumberOfNodes(T.right)

    def deleteNode(self, value):
        nodeToDelete = self.findNode(value)
        if nodeToDelete is None:
            return False  # Node not found

        if nodeToDelete.left is None:
            self.transplant(nodeToDelete, nodeToDelete.right)
        elif nodeToDelete.right is None:
            self.transplant(nodeToDelete, nodeToDelete.left)
        else:
            successor = self.treeSuccessor(nodeToDelete)
            if successor.parent != nodeToDelete:
                self.transplant(successor, successor.right)
                successor.right = nodeToDelete.right
                successor.right.parent = successor
            self.transplant(nodeToDelete, successor)
            successor.left = nodeToDelete.left
            successor.left.parent = successor

        del nodeToDelete
        return True

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def treeSuccessor(self, T):
        if T.right is not None:
            return self.treeMinimum(T.right)
        else:
            temp = T.parent
            while temp is not None and T == temp.right:
                T = temp
                temp = temp.parent
            return temp

    def inOrderTraversal(self, T):
        if T is None:
            with open('inputs/user_data.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(["User Name", "Email", "Password", "Address", "Type"])
            return
        
        # Storing data in file recursively
        with open('inputs/user_data.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow([T.data.username, T.data.email, T.data.password, T.data.address, "Customer"])
        
        self.inOrderTraversal(T.left)
        print(T.data.username, end=" ")
        self.inOrderTraversal(T.right)
