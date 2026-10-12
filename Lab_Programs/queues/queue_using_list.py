capacity=5
queue=[None]*capacity
front=-1
rear=-1

def enqueue(queue,data,front,rear):
    if rear==capacity-1:
        print("Queue overflow")
        return front,rear
    if front==-1:
        front=0
    rear+=1
    queue[rear]=data
    return front,rear

def dequeue(queue,front,rear):
    if front==-1:
        print("Queue Overflow")
        return front,rear
    value=queue[front]
    queue[front]=None

    if front==rear:
        front=-1
        rear=-1
    else:
        front+=1
    print("Deleted ele:",value)
    return front,rear

def peek(queue,front):
    if front==-1:
        print("Queue is empty")
        return
    print("Front ele:",queue[front])

def isEmpty(front):
    return front==-1

def isFull(rear):
    return rear==capacity-1

def display(queue,front,rear):
    if front==-1:
        print("Queue is empty")
        return
    print("Queue ele from front to rear:")
    for i in range(front,rear+1):
        print(f"[{queue[i]}]",end="")
    print()

while True:
    print("\n===== QUEUE USING LIST =====")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if Full")
    print("6. Display")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter the element: "))
        front, rear = enqueue(queue, data, front, rear)

    elif choice == "2":
        front, rear = dequeue(queue, front, rear)

    elif choice == "3":
        peek(queue, front)

    elif choice == "4":
        if isEmpty(front):
            print("Queue is empty")
        else:
            print("Queue is not empty")

    elif choice == "5":
        if isFull(rear):
            print("Queue is full")
        else:
            print("Queue is not full")

    elif choice == "6":
        display(queue, front, rear)

    elif choice == "7":
        print("Program terminated")
        break

    else:
        print("Invalid choice")