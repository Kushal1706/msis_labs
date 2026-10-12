class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

root=None

def insert(root,data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left=insert(root.left,data)
    elif data > root.data:
        root.right=insert(root.right,data)
    else:
        print("Duplicate values are not allowed")
    return root

def search(root,value):
    if root is None:
        return False
    
    if root.data==value:
        return True
    elif value<root.data:
        return search(root.left,value)
    else:
        return search(root.right,value)
    
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def level_order(root):
    if root is None:
        print("Tree is empty")
        return
    queue=[root]
    front=0
    while front<len(queue):
        curr=queue[front]
        front+=1
        print(curr.data,end=" ")

        if curr.left is not None:
            queue.append(curr.left)
        
        if curr.right is not None:
            queue.append(curr.right)

def find_min(root):
    if root is None:
        return None
    
    curr=root
    while curr.left is not None:
        curr=curr.left
    
    return curr.data

def find_max(root):
    if root is None:
        return None
    
    curr=root
    while curr.right is not None:
        curr=curr.right
    return curr.data

def height(root):
    if root is None:
        return -1
    
    left_height=height(root.left)
    right_height=height(root.right)

    return 1+max(left_height,right_height)

def find_min_node(root):
    curr=root
    while curr.left is not None:
        curr=curr.left
    return curr

def delete(root,value):
    if root is None:
        return None

    if value<root.data:
        root.left=delete(root.left,value)
    elif value>root.data:
        root.right=delete(root.right,value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        successor=find_min_node(root.right)
        root.data=successor.data
        root.right=delete(root.right,successor.data)
    return root

while True:
    print("\n\n===== BINARY SEARCH TREE =====")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Level order traversal")
    print("7. Find Minimum")
    print("8. Find Maximum")
    print("9. Find Height")
    print("10. Delete")
    print("11. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        data=int(input("Enter value to insert:"))
        root=insert(root,data)
    elif choice=="2":
        key=int(input("Enter value to search:"))
        if search(root,key):
            print("Element found")
        else:
            print("Element not found")
    elif choice=="3":
        if root is None:
            print("Tree is empty")
        else:
            print("Inorder traversal:")
            inorder(root)
    elif choice=="4":
        if root is None:
            print("Tree is empty")
        else:
            print("Preorder traversal:")
            preorder(root)

    elif choice == "5":
        if root is None:
            print("Tree is empty")
        else:
            print("Postorder traversal:")
            postorder(root)
    elif choice == "6":
        print("Level order traversal:")
        level_order(root)

    elif choice == "7":
        minimum = find_min(root)

        if minimum is None:
            print("Tree is empty")
        else:
            print("Minimum value:", minimum)

    elif choice == "8":
        maximum = find_max(root)

        if maximum is None:
            print("Tree is empty")
        else:
            print("Maximum value:", maximum)

    elif choice == "9":
        print("Height of tree:", height(root))
    
    elif choice=="10":
        value=int(input("Enter a value to delete:"))

        if not search(root,value):
            print("Element not found")
        else:
            root=delete(root,value)
            print("Ele deleted:",value)

    elif choice == "11":
        print("Program terminated")
        break

    else:
        print("Invalid choice")    