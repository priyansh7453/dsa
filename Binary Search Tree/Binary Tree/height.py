<<<<<<< HEAD
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1  # use 0 if height is defined as number of nodes
    return 1 + max(height(root.left), height(root.right))

def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(4)
root.left.left.left = Node(4)

print(height(root))  # Output: 2
print(size(root))
=======
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1  # use 0 if height is defined as number of nodes
    return 1 + max(height(root.left), height(root.right))

def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(4)
root.left.left.left = Node(4)

print(height(root))  # Output: 2
print(size(root))
>>>>>>> 6719c2f4d4104a6c6c9f4d821bcff7884be0054c
