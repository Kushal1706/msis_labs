class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

front=None
rear=None

def enqueue(front,rear,data):
    new_node=Node(data)

    if front is None:
        front=new_node
        rear=new_node

    rear.next=new_node
    rear=new_node
    return front,rear

def dequeue(front,rear):
    if front is None:
        print("Queue Underflow: Queue is empty")
        return front,rear
    
    value=front.data
    front=front.next

    if front is None:
        rear=None
    print("Dleted ele:",value)
    return front,rear

def peek(front):
    if front is None:
        print("Queue is empty")
        return 
    
    print("Front ele:",front.data)

def isEmpty(front):
    return front is None

def display(front):
    if front is None:
        print("Queue is empty")
        return
    
    print("Queue ele from front to rear:")
    curr=front

    while curr is not None:
        print(curr.data)
        curr=curr.next

while True:
    print("\n===== QUEUE USING LINKED LIST =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter the element: "))
        front, rear = enqueue(front, rear, data)

    elif choice == "2":
        front, rear = dequeue(front, rear)

    elif choice == "3":
        peek(front)

    elif choice == "4":
        if isEmpty(front):
            print("Queue is empty")
        else:
            print("Queue is not empty")

    elif choice == "5":
        display(front)

    elif choice == "6":
        print("Program terminated")
        break

    else:
        print("Invalid choice")