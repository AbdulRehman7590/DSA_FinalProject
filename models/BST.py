# ----------------------- Node -------------------------------- #
class Node:
    def __init__(self, value, parentNode=None):
        self.data = value
        self.right = None
        self.left = None
        self.parent = parentNode

# ------------------------ Bst -------------------------------- #
class BST:
    def __init__(self):
        self.root = None
        self.counter = 0

    # ---------------------- Insert --------------------------- #
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

    # ---------------------- Search --------------------------- #
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

    # -------------------- Total nodes ------------------------ #
    def NumberOfNodes(self, T):
        if T is None:
            return 0
        return 1 + self.NumberOfNodes(T.left) + self.NumberOfNodes(T.right)

    # ---------------------- Delete --------------------------- #
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

    # ------------------- Pre Order Traversal ------------------- #
    def preOrderTraversal(self, T):
        nodes = []
        if T is None:
            return nodes

        nodes.append(T.data)
        nodes += self.preOrderTraversal(T.left)
        nodes += self.preOrderTraversal(T.right)

        return nodes

    # ------------------- In Order Traversal -------------------- #
    def inOrderTraversal(self, T, idx):
        if T is None:
            return None

        left = self.inOrderTraversal(T.left, idx)
        if left is not None:
            if hasattr(left, 'data'):
                return left.data

        if self.counter == idx:
            if hasattr(T, 'data'):
                return T.data

        self.counter += 1

        right = self.inOrderTraversal(T.right, idx)
        if right is not None:
            if hasattr(right, 'data'):
                return right.data

        return None


