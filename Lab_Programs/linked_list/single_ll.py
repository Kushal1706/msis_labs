class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=None

def insert_beginning(head,data):
    new_node=Node(data)
    new_node.next=head
    head=new_node
    return head

def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        head=new_node
        return head
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=new_node
    return head

def insert_position(head,data,pos):
    if pos<1:
        print("Invalid pos")
        return head
    if pos==1:
        new_node=Node(data)
        new_node.next=head
        head=new_node
        return head
    curr=head
    for i in range(pos-2):
        if curr is None:
            print("Invalis pos")
            return head
        curr=curr.next
    if curr is None:
        print("Invalid pos")
        return head
    new_node=Node(data)
    new_node.next=curr.next
    curr.next=new_node
    return head

def delete_beginning(head):
    if head is None:
        print("List is empty")
        return head
    head=head.next
    return head

def delete_end(head):
    if head is None:
        print("List is Empty")
        return head
    if head.next is None:
        head=None
        return head
    curr=head
    while curr.next.next is not None:
        curr=curr.next
    curr.next=None
    return head

def delete_position(head,pos):
    if head is None:
        print("List is Empty")
        return head
    if pos < 1:
        print("Invalid pos")
        return head
    if pos==1:
        head=head.next
        return head
    curr=head
    for i in range(pos-2):
        if curr is None:
            print("Invalid pos")
            return head
        curr=curr.next

    if curr is None or curr.next is None:
        print("Invalid pos")
        return head
    curr.next=curr.next.next
    return head

def reverse(head):
    prev=None
    curr=head

    while curr is not None:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    head=prev
    return head

def display(head):
    if head is None:
        print("List is Empty")
        return
    
    curr=head
    while curr is not None:
        print(curr.data,end="->")
        curr=curr.next
    print("None")

while True:
    print("\n====Single linked list===")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete at beginning")
    print("5. Delete at end")
    print("6. Delete at position")
    print("7. Display list")
    print("8. Reverse list")
    print("9. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        data=int(input("Enter data:"))
        head=insert_beginning(head,data)
    
    elif choice==2:
        data=int(input("Enter the data:"))
        head=insert_end(head,data)

    elif choice==3:
        data=int(input("Enter data:"))
        pos=int(input("Enter pos:"))
        head=insert_position(head,data,pos)
    elif choice == 4:
        head = delete_beginning(head)

    elif choice == 5:
        head = delete_end(head)

    elif choice == 6:
        position = int(input("Enter position: "))
        head = delete_position(head, position)

    elif choice == 7:
        display(head)

    elif choice == 8:
        head = reverse(head)
        print("Linked list reversed")

    elif choice == 9:
        print("Program terminated")
        break

    else:
        print("Invalid choice")