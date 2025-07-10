class Node:
    def __init__(self,data):
        # Constructor to initialize a new node with data
        self.data = data
        self.next = None
        
        
        
def search(head,element):
    # Function to search for a node with a given value in the linked list
    current = head
    while current is not None:
        if current.data == element: 
            return "Yes"
        current = current.next
    return "No"

def length(head):
    # Function to calculate the length of the linked list
    current = head
    if current is None:
        print("the list is empty")
    count = 0
    while current is not None:
        count += 1
        current = current.next
    # print(count)
        
    
if __name__ == "__main__":
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 88 -> 550 ->760
    # head = Node(10)
    # head.next = Node(20)
    # head.next.next = Node(30)
    # head.next.next.next = Node(88)
    # head.next.next.next.next = Node(550)
    # head.next.next.next.next.next = Node(760)
    # key = 80
    # print(search(head, key))
    length(None)