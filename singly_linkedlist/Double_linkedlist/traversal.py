class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
        
def traversal(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next


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
    traversal(head)