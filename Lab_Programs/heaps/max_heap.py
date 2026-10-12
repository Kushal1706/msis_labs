capacity=8
heap=[None]*capacity
size=0

def insert(heap,data,size,capacity):
    if size==capacity:
        print("Heap overflow")
        return size
    idx=size
    heap[idx]=data
    size+=1

    while idx>0:
        parent=(idx-1)//2
        
        if heap[parent]<heap[idx]:
            heap[parent],heap[idx]=heap[idx],heap[parent]
            idx=parent
        else:
            break
    print("Elemented inserted:",data)
    return size

def delete_max(heap,size):
    if size==0:
        print("Heap underflow")
        return size
    
    maximum=heap[0]
    heap[0]=heap[size-1]
    heap[size-1]=None
    size-=1

    idx=0
    while True:
        left=2*idx+1
        right=2*idx+2
        largest=idx

        if left<size and heap[left]>heap[largest]:
            largest=left
        if right<size and heap[right] > heap[largest]:
            largest=right
        if largest !=idx:
            heap[idx],heap[largest]=heap[largest],heap[idx]
            idx=largest
        else:
            break
    
    print('Deleted max ele:',maximum)
    return size

def display(heap,size):
    if size==0:
        print("Heap is empty")
        return
    print("Heap ele:",heap[:size])

def peek_max(heap,size):
    if size==0:
        print("Heap is empty")
    else:
        print("Max ele:",heap[0])

while True:
    print("\n--- MAX HEAP MENU ---")
    print("1. Insert")
    print("2. Delete Maximum")
    print("3. Display Heap")
    print("4. Peek Maximum")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter element: "))
        size = insert(heap, data, size, capacity)

    elif choice == "2":
        size = delete_max(heap, size)

    elif choice == "3":
        display(heap, size)

    elif choice == "4":
        peek_max(heap, size)

    elif choice == "5":
        print("Program terminated")
        break

    else:
        print("Invalid choice")