capacity=8
tree=[None]*capacity

def insert(tree,data):
    idx=0
    while idx < capacity:
        if tree[idx] is None:
            tree[idx]=data
            print("Ele inserted:",data)
            return
        
        elif data<tree[idx]:
            idx=2*idx+1
        elif data>tree[idx]:
            idx=2*idx+2
        else:
            print("Duplicate values are not allowed")
            return
    print("Insertion failed:Arracy capacity full")

def search(tree,key):
    idx=0

    while idx<capacity and tree[idx] is not None:
        if tree[idx]==key:
            return idx
        
        elif key<tree[idx]:
            idx=2*idx+1
        else:
            idx=2*idx+2
    return -1

def inorder(tree,idx):
    if idx>=capacity or tree[idx] is None:
        return
    
    inorder(tree,2*idx+1)
    print(tree[idx],end=" ")
    inorder(tree,2*idx+2)

def preorder(tree,idx):
    if idx >=capacity or tree[idx] is None:
        return
    
    print(tree[idx],end=" ")
    preorder(tree,2*idx+1)
    preorder(tree,2*idx+2)

def postorder(tree,idx):
    if idx>=capacity or tree[idx] is None:
        return
    
    postorder(tree,2*idx+1)
    postorder(tree,2*idx+2)
    print(tree[idx],end=" ")

def level_order(tree):
    if tree[0] is None:
        print("Tree is empty")
        return
    
    print("Level order traversal:")
    for value in tree:
        if value is not None:
            print(value,end=" ")

def find_min(tree):
    if tree[0] is None:
        return None
    
    idx=0
    while True:
        left=2*idx+1
        if left>=capacity or tree[left] is None:
            return tree[idx]
        idx=left

def find_max(tree):
    if tree[0] is None:
        return None
    
    idx=0
    while True:
        right=2*idx+2
        if right>=capacity or tree[right] is None:
            return tree[idx]
        idx=right

def display_array(tree):
    print("Array representation:")
    print(tree)

while True:
    print("\n\n===== BST USING ARRAY =====")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder Traversal")
    print("4. Preorder Traversal")
    print("5. Postorder Traversal")
    print("6. Level Order Traversal")
    print("7. Find Minimum")
    print("8. Find Maximum")
    print("9. Display Array")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter value to insert: "))
        insert(tree, data)

    elif choice == "2":
        key = int(input("Enter value to search: "))
        index = search(tree, key)

        if index != -1:
            print("Element found at index:", index)
        else:
            print("Element not found")

    elif choice == "3":
        if tree[0] is None:
            print("Tree is empty")
        else:
            print("Inorder traversal:")
            inorder(tree, 0)
            print()

    elif choice == "4":
        if tree[0] is None:
            print("Tree is empty")
        else:
            print("Preorder traversal:")
            preorder(tree, 0)
            print()

    elif choice == "5":
        if tree[0] is None:
            print("Tree is empty")
        else:
            print("Postorder traversal:")
            postorder(tree, 0)
            print()

    elif choice == "6":
        level_order(tree)
        print()

    elif choice == "7":
        value = find_min(tree)

        if value is None:
            print("Tree is empty")
        else:
            print("Minimum value:", value)

    elif choice == "8":
        value = find_max(tree)

        if value is None:
            print("Tree is empty")
        else:
            print("Maximum value:", value)

    elif choice == "9":
        display_array(tree)

    elif choice == "10":
        print("Program terminated")
        break

    else:
        print("Invalid choice")    