class BinarySearchTree:
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insertRoot(self, val):
        if self.root is None:
            self.root = self.TreeNode(val)

    def insertLeft(self, prev, val):
        if self.root is None:
            return
        self.traverseLeft(self.root, prev, val)

    def traverseLeft(self, node, prev, val):
        if node is None:
            return
        if node.value == prev:
            if node.left is None:
                node.left = self.TreeNode(val)
            else:
                print("Left child already exists.")
        else:
            self.traverseLeft(node.left, prev, val)
            self.traverseLeft(node.right, prev, val)

    def insertRight(self, prev, val):
        if self.root is None:
            return
        self.traverseRight(self.root, prev, val)

    def traverseRight(self, node, prev, val):
        if node is None:
            return
        if prev == node.value:
            if node.left is not None: 
                newnode = self.TreeNode(val)
                node.right = newnode
                return
            else:
                print("Right child already exists.")
        self.traverseRight(node.right, prev, val)
        self.traverseRight(node.left, prev, val)

    def display(self):
        self.displayTraverse(self.root, "Root Node: ")

    def displayTraverse(self, node, details):
        if node is None:
            return
        print(details + str(node.value))
        self.displayTraverse(node.left, "Left child of " + str(node.value))
        self.displayTraverse(node.right, "Right child of " + str(node.value))


# Example usage
bst = BinarySearchTree()
bst.insertRoot(10)
bst.insertLeft(10, 5)
bst.insertRight(10, 7)
bst.insertLeft(5, 3)
bst.insertRight(5, 4)
bst.display()
