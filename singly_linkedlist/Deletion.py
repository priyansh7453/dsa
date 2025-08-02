from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def deletion_start(head):
    head = head.next

def deletion_end(head):
    current = head
    while current.next is not None:
        current = current.next
    current.next = None
    traversal(head)
    
def deletion_position(head,pos):
    current = head
    for i in range(1,pos-1):
        current = current.next
    current.next = current.next.next
    traversal(head)

if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 88  -> 550 ->760
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    # deletion_start(head)
    deletion_end(head)
    # deletion_position(head, 3)