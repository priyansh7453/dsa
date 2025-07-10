from traversal import traversal
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
        
def insertion_first(head,key):
    new_node = Node(key)
    new_node.next = head
    head.prev = new_node
    
def insertion_end(head,key):
    new_node = Node(key)
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    new_node.prev = current
    
    
def insertion_pos(head,key,pos):
    new_node = Node(key)
    current = head
    for i in range(1,pos-1):
        current = current.next
    # Set the prev of newnode to curr
    new_node.prev = current
    # Set the next of new node to next of curr
    new_node.next = current.next
    # Update the next of current node to new node
    current.next = new_node
    traversal(head)

if __name__ == "__main__":
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(125)
    second = Node(200)
    third = Node(364)
    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    # traversal(head)
    # insertion_first(head,50)
    # insertion_end(head, 500)
    insertion_pos(head, 500, 3)