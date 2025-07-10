class Node:
    def __init__(self,data):
        # Constructor to initialize a new node with data
        self.data = data
        self.next = None
        
def traversal(head):
    # Function to print the linked list
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

#driven code
def main():
    # Create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40 -> 50 ->60
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(88)
    head.next.next.next.next = Node(550)
    head.next.next.next.next.next = Node(760)
    
    traversal(head)
    
if __name__ == "__main__":
    main()