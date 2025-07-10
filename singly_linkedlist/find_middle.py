from traversal import traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)



if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 88 -> 550 ->760
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    head.next.next.next.next.next.next = Node(6660)
    head.next.next.next.next.next.next.next = Node(111)
    traversal(head)
    find_middle(head)