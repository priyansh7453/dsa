from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def reverse(head):
    prev = None
    current = head
    while current is not None:
        # store element
        nxt_Node = current.next
        current.next = prev
        
        # Move pointer one position ahead
        prev = current
        current = nxt_Node

    traversal(prev)


if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 88 -> 550 ->760
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    reverse(head)  # Output: 760 ->