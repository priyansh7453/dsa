<<<<<<< HEAD
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# ✅ 1. Insert node in BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# ✅ 3. Min node in BST
def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

# ✅ 3. Min node in BST
def maxValueNode(node):
    current = node
    while current.right:
        current = current.right
    return current

# ✅ 3. Delete node in BST
def getsuccer(root):
    curr = root.right
    if curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def delete_node(root,key):
    if root is None:
        return root
    
    if root.data > key:
        root.left = delete_node(root.left, key)
        
    elif root.data < key:
        root.right = delete_node(root.right, key)
        
    # if the data is match  
    else :
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:
            succer = getsuccer(root)
            root.data = succer.data
            root.left = delete_node(root.left , succer.data)
    return root

# ✅ 4. Inorder Traversal (sorted order)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    # ✅ 1. Create BST
    root = None
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        root = insert(root, k)
    
    min = minValueNode(root)
    print("Min Node:", min.data)
    max = maxValueNode(root)
    print("Max Node:", max.data)
    
    dele = delete_node(root,60)
    print("After Deletion:")
=======
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# ✅ 1. Insert node in BST
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# ✅ 3. Min node in BST
def minValueNode(node):
    current = node
    while current.left:
        current = current.left
    return current

# ✅ 3. Min node in BST
def maxValueNode(node):
    current = node
    while current.right:
        current = current.right
    return current

# ✅ 3. Delete node in BST

def getsuccer(root):
    curr = root.right
    if curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def delete_node(root,key):
    if root is None:
        return root
    
    if root.data > key:
        root.left = delete_node(root.left, key)
        
    elif root.data < key:
        root.right = delete_node(root.right, key)
        
    # if the data is match  
    else :
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        else:
            succer = getsuccer(root)
            root.data = succer.data
            root.left = delete_node(root.left , succer.data)
    return root

# ✅ 4. Inorder Traversal (sorted order)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


if __name__ == "__main__":
    # ✅ 1. Create BST
    root = None
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        root = insert(root, k)
    
    min = minValueNode(root)
    print("Min Node:", min.data)
    max = maxValueNode(root)
    print("Max Node:", max.data)
    
    dele = delete_node(root,60)
    print("After Deletion:")
>>>>>>> 6719c2f4d4104a6c6c9f4d821bcff7884be0054c
    inorder(dele)  # Output: 20 30 40 50 70 80