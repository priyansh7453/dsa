from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Insertion_front(head,key):
    new_node = Node(key)
    if head is None:
        head = new_node
    new_node.next = head
    head = new_node

def Insertion_end(head,key):
    new_node = Node(key)
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    
    traversal(head)

def Insertion_position(head,pos,key):
    new_node = Node(key)
    current = head
    for i in range(1,pos-1):
        current = current.next
    new_node.next = current.next
    current.next = new_node

    traversal(head)

if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 88 -> 550 ->760
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    
    # Insertion_front(head, 1000)
    # Insertion_end(head, 1000)
    Insertion_position(head, 3, 1000)