capacity=5
queue=[None]*capacity
front=0
rear=0
size=0

def enqueue(queue, front, rear, size, capacity, data):
        if size == capacity:
            new_capacity = capacity * 2
            new_queue = [None] * new_capacity

            # Copy elements in FIFO order
            for i in range(size):
                new_queue[i] = queue[(front + i) % capacity]

            queue = new_queue
            capacity = new_capacity
            front = 0
            rear = size

            print("Queue capacity doubled to:", capacity)

        queue[rear] = data
        rear = (rear + 1) % capacity
        size += 1

        print("Element enqueued:", data)
        return queue, front, rear, size, capacity

# Remove an element from the front
def dequeue(queue, front, rear, size, capacity):
    if size == 0:
        print("Queue Underflow")
        return queue, front, rear, size, capacity

    value = queue[front]
    queue[front] = None

    front = (front + 1) % capacity
    size -= 1

    if size == 0:
        front = 0
        rear = 0

    print("Dequeued element:", value)
    return queue, front, rear, size, capacity

# View the front element
def peek(queue, front, size):
    if size == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])

# Display queue elements in FIFO order
def display(queue, front, size, capacity):
    if size == 0:
        print("Queue is empty")
        return

    print("Queue elements (front to rear):")

    for i in range(size):
        index = (front + i) % capacity
        print(queue[index], end=" ")

    print()

# Menu-driven program
while True:
    print("\n--- DYNAMIC QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Display Capacity")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter element: "))
        queue, front, rear, size, capacity = enqueue(
            queue, front, rear, size, capacity, data
        )

    elif choice == "2":
        queue, front, rear, size, capacity = dequeue(
            queue, front, rear, size, capacity
        )

    elif choice == "3":
        peek(queue, front, size)

    elif choice == "4":
        display(queue, front, size, capacity)

    elif choice == "5":
        print("Current capacity:", capacity)
        print("Number of elements:", size)

    elif choice == "6":
        print("Program terminated")
        break

    else:
        print("Invalid choice")