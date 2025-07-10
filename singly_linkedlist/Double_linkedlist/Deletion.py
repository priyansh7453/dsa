from traversal import traversal

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        

def deletion_first(head):
    current = head
    head = head.next
    head.prev = None
    # traversal(head)
    
def deletion_end(head):
    current = head
    while current.next.next is not None:
        current = current.next
    current.next.prev.next = None
    current.next = None

def deletion_pos(head,pos):
    current = head
    for i in range(1,pos-1):
        current = current.next
    current.next = current.next.next
    current.next.next.prev = current
    
    

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
    deletion_first(head)
    deletion_end(head)
    deletion_pos(head,2)