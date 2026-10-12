class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

head=None
tail=None

def insert_beginning(head,tail,data):
    new_node=Node(data)
    if head is None:
        head=new_node
        tail=new_node
        return head,tail
    new_node.next=head
    head.prev=new_node
    head=new_node
    return head,tail

def insert_end(head,tail,data):
    new_node=Node(data)

    if tail is None:
        head=new_node
        tail=new_node
        return head,tail
    tail.next=new_node
    new_node.prev=tail

    tail=new_node
    return head,tail

def insert_position(head,tail,data,pos):
    if pos<1:
        print("Invalid pos")
        return head,tail
    if pos==1:
        return insert_beginning(head,tail,data)
    curr=head
    for i in range(pos-2):
        if curr is None:
            print("Invalid pos")
            return head,tail
        curr=curr.next
    if curr is None:
        print("Invalid pos")
        return head,tail
    new_node=Node(data)
    next_node=curr.next

    new_node.prev=curr
    new_node.next=next_node

    curr.next=new_node
    next_node.prev=new_node
    return head,tail

def delete_beginning(head,tail):
    if head is None:
        print("List is Empty")
        return head,tail
    if head==tail:
        head=None
        tail=None
        return head,tail
    head=head.next
    head.prev=None
    return head,tail

def delete_end(head,tail):
    if tail is None:
        print("List is Empty")
        return head,tail
    if head==tail:
        head=None
        tail=None
        return head,tail
    tail=tail.prev
    tail.next=None
    return head,tail

def delete_position(head,tail,pos):
    if head is None:
        print("List is empty")
        return head,tail
    if pos<1:
        print("Invalid pos")
        return head,tail
    if pos==1:
        return delete_beginning(head,tail)
    curr=head
    for i in range(pos-1):
        if curr is None:
            print("Invalid pos")
            return head,tail
        curr=curr.next
    if curr is None:
        print("Invalid pos")
        return head,tail
    if curr==tail:
        return delete_end(head,tail)
    
    curr.prev.next=curr.next
    curr.next.prev=curr.prev

    return head,tail

def display_forward(head):
    if head is None:
        print("List is Empty")
        return 
    curr=head
    while curr is not None:
        print(curr.data,end="<->")
        curr=curr.next
    print("None")

def display_backward(tail):
    if tail is None:
        print("List is empty")
        return
    curr=tail
    while curr is not None:
        print(curr.data,end="<->")
        curr=curr.prev
    print("None")

while True:
    print("\n===== DOUBLY LINKED LIST MENU =====")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete at position")
    print("7. Display forward")
    print("8. Display backward")
    print("9. Exit")  
    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        head, tail = insert_beginning(head, tail, data)

    elif choice == 2:
        data = int(input("Enter data: "))
        head, tail = insert_end(head, tail, data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        head, tail = insert_position(
            head, tail, data, position
        )

    elif choice == 4:
        head, tail = delete_beginning(head, tail)

    elif choice == 5:
        head, tail = delete_end(head, tail)

    elif choice == 6:
        position = int(input("Enter position: "))
        head, tail = delete_position(
            head, tail, position
        )

    elif choice == 7:
        display_forward(head)

    elif choice == 8:
        display_backward(tail)

    elif choice == 9:
        print("Program terminated")
        break

    else:
        print("Invalid choice")