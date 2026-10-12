capacity=8
heap=[None]*capacity
size=0

def insert(heap, data, size, capacity):
        if size == capacity:
            print("Heap Overflow")
            return size

        index = size
        heap[index] = data
        size += 1

        # Heapify up
        while index > 0:
            parent = (index - 1) // 2

            if heap[parent] > heap[index]:
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent
            else:
                break

        print("Element inserted:", data)
        return size

# Delete the minimum element (root)
def delete_min(heap, size):
    if size == 0:
        print("Heap Underflow")
        return size

    minimum = heap[0]
    heap[0] = heap[size - 1]
    heap[size - 1] = None
    size -= 1

    # Heapify down
    index = 0

    while True:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < size and heap[left] < heap[smallest]:
            smallest = left

        if right < size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != index:
            heap[index], heap[smallest] = heap[smallest], heap[index]
            index = smallest
        else:
            break

    print("Deleted minimum element:", minimum)
    return size

# Display the heap
def display(heap, size):
    if size == 0:
        print("Heap is empty")
        return

    print("Heap elements:", heap[:size])

# Display the minimum element
def peek_min(heap, size):
    if size == 0:
        print("Heap is empty")
    else:
        print("Minimum element:", heap[0])

# Menu-driven program
while True:
    print("\n--- MIN HEAP MENU ---")
    print("1. Insert")
    print("2. Delete Minimum")
    print("3. Display Heap")
    print("4. Peek Minimum")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter element: "))
        size = insert(heap, data, size, capacity)

    elif choice == "2":
        size = delete_min(heap, size)

    elif choice == "3":
        display(heap, size)

    elif choice == "4":
        peek_min(heap, size)

    elif choice == "5":
        print("Program terminated")
        break

    else:
        print("Invalid choice")