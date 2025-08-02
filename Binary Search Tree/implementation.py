<<<<<<< HEAD
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,key):
    if root is None:
        return Node(key)
    
    if root.data > key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
        
    return root
    
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)
        
def post_order(root):
    if root:
        post_order(root.left)
        pre_order(root.right)
        print(root.data, end=" ")
        
def find(root,key):
    if root is None or root.data == key:
        return root
    if root.data > key:
        return find(root.left, key)
    return find(root.right, key)

def find_iterative(root, key):
    while root:
        if root.data == key:
            return root
        elif key < root.data:
            root = root.left
        else:
            root = root.right
    return None
        
if __name__ == "__main__":
    # root = Node(50)
    # insert(root, 30)
    # insert(root, 20)
    # insert(root, 40)
    # insert(root, 70)
    # insert(root, 60)
    # insert(root, 80)
    root = None
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        root = insert(root, k)
    
    print("In order traversal of the BST is")
    in_order(root)
    print("\nPre order traversal of the BST is")
    pre_order(root)
    print("\nPost order traversal of the BST is")
    post_order(root)
    print("\nThe search element is ")
    found_element = find(root,77)
    if found_element:
        print("Element is present in the BST")
    else:
        print("Element is not present in the BST")
        
    ans=find_iterative(root,60)
    if ans:
        print("Element is present in the BST")
    else:
=======
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root,key):
    if root is None:
        return Node(key)
    
    if root.data > key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
        
    return root
    
def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

def pre_order(root):
    if root:
        print(root.data, end=" ")
        pre_order(root.left)
        pre_order(root.right)
        
def post_order(root):
    if root:
        post_order(root.left)
        pre_order(root.right)
        print(root.data, end=" ")
        
def find(root,key):
    if root is None or root.data == key:
        return root
    if root.data > key:
        return find(root.left, key)
    return find(root.right, key)

def find_iterative(root, key):
    while root:
        if root.data == key:
            return root
        elif key < root.data:
            root = root.left
        else:
            root = root.right
    return None
        
if __name__ == "__main__":
    # root = Node(50)
    # insert(root, 30)
    # insert(root, 20)
    # insert(root, 40)
    # insert(root, 70)
    # insert(root, 60)
    # insert(root, 80)
    root = None
    keys = [50, 30, 70, 20, 40, 60, 80]
    for k in keys:
        root = insert(root, k)
    
    print("In order traversal of the BST is")
    in_order(root)
    print("\nPre order traversal of the BST is")
    pre_order(root)
    print("\nPost order traversal of the BST is")
    post_order(root)
    print("\nThe search element is ")
    found_element = find(root,77)
    if found_element:
        print("Element is present in the BST")
    else:
        print("Element is not present in the BST")
        
        
    ans=find_iterative(root,60)
    if ans:
        print("Element is present in the BST")
    else:
>>>>>>> 6719c2f4d4104a6c6c9f4d821bcff7884be0054c
        print("Element is not present in the BST")