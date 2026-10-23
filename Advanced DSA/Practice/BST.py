class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def addElement(self,root,data):
        if root is None:
            return Node(data)

        if data<root.data:
            root.left = self.addElement(root.left,data)
        elif data>root.data:
            root.right = self.addElement(root.right,data)
        else:
            print("Duplicate elements are not allowed")
        return root

    def find_min_node(self,root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root
        

    def Delete(self,root,key):
        if root is None:
            return None

        if key<root.data:
            root.left = self.Delete(root.left,key)
        elif key > root.data:
            root.right = self.Delete(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            if root.right is not None and root.left is not None:
                successor = self.find_min_node(root.right)
                root.data = successor.data
                root.right = self.Delete(root.right,successor.data)
        return root

    def find_max(self,root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right

        return root.data

    def preored(self,root):
        if root is None:
            return None
        print(root.data,end=" ")
        self.preored(root.left)
        self.preored(root.right)
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)


bst = BST()
bst.root = bst.addElement(bst.root,20)
bst.root = bst.addElement(bst.root,100)
bst.root = bst.addElement(bst.root,1)
bst.preored(bst.root)
bst.inorder(bst.root)
