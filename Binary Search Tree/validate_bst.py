<<<<<<< HEAD
# Python program to check if a tree is BST using Inorder Traversal

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
def isBST(root, min_val, max_val):
    if root is None:
        return True
    
    if root.data > min_val and root.data <max_val:
        lef = isBST(root.left, min_val, root.data)
        righ = isBST(root.right, root.data, max_val)
        return lef and righ
    else:
        return False
    


if __name__ == "__main__":
    # Create a sample binary tree
# Tree:
#       10
#      /  \
#     5    15

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    print("Is BST:", isBST(root, float('-inf'), float('inf')))
    # if isBST(root):
    #     print("True")
    # else:
=======
# Python program to check if a tree is BST using Inorder Traversal

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
def isBST(root, min_val, max_val):
    if root is None:
        return True
    
    if root.data > min_val and root.data <max_val:
        lef = isBST(root.left, min_val, root.data)
        righ = isBST(root.right, root.data, max_val)
        return lef and righ
    else:
        return False
    


if __name__ == "__main__":
    # Create a sample binary tree
# Tree:
#       10
#      /  \
#     5    15

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)

    print("Is BST:", isBST(root, float('-inf'), float('inf')))
    # if isBST(root):
    #     print("True")
    # else:
>>>>>>> 6719c2f4d4104a6c6c9f4d821bcff7884be0054c
    #     print("False")