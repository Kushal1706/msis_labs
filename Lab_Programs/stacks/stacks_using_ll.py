class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

top=None

def push(top,data):
    new_node=Node(data)
    new_node.next=top
    top=new_node
    return top

def pop(top):
    if top is None:
        print("Stack Underflow")
        return top
    value=top.data
    top=top.next
    print("Poped ele:",value)
    return top

def peek(top):
    if top is None:
        print("Stack is empty")
        return
    print("Top element:",top.data)

def isEmpty(top):
    return top is None

def display(top):
    if top is None:
        print("Stack is empty")
        return
    print("Stack ele from top to bottom:")
    curr=top
    while curr is not None:
        print(curr.data)
        curr=curr.next

while True:
    print("\n===== STACK USING LINKED LIST =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Display")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter the element: "))
        top = push(top, data)

    elif choice == "2":
        top = pop(top)

    elif choice == "3":
        peek(top)

    elif choice == "4":
        if isEmpty(top):
            print("Stack is empty")
        else:
            print("Stack is not empty")

    elif choice == "5":
        display(top)

    elif choice == "6":
        print("Program terminated")
        break

    else:
        print("Invalid choice")