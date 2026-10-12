capacity=5
stack=[None]*capacity
top=-1

def push(stack, top, capacity, data):
        if top == capacity - 1:
            new_capacity = capacity * 2
            new_stack = [None] * new_capacity

            for i in range(capacity):
                new_stack[i] = stack[i]

            stack = new_stack
            capacity = new_capacity

            print("Stack capacity doubled to:", capacity)

        top += 1
        stack[top] = data

        print("Element pushed:", data)
        return stack, top, capacity

# Pop an element
def pop(stack, top, capacity):
    if top == -1:
        print("Stack Underflow")
        return stack, top, capacity

    value = stack[top]
    stack[top] = None
    top -= 1

    print("Popped element:", value)
    return stack, top, capacity

# View the top element
def peek(stack, top):
    if top == -1:
        print("Stack is empty")
    else:
        print("Top element:", stack[top])

# Display stack elements
def display(stack, top):
    if top == -1:
        print("Stack is empty")
        return

    print("Stack elements (top to bottom):")
    for i in range(top, -1, -1):
        print(stack[i], end=" ")
    print()

# Menu-driven program
while True:
    print("\n--- DYNAMIC STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Display Capacity")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        data = int(input("Enter element: "))
        stack, top, capacity = push(
            stack, top, capacity, data
        )

    elif choice == "2":
        stack, top, capacity = pop(
            stack, top, capacity
        )

    elif choice == "3":
        peek(stack, top)

    elif choice == "4":
        display(stack, top)

    elif choice == "5":
        print("Current capacity:", capacity)
        print("Number of elements:", top + 1)

    elif choice == "6":
        print("Program terminated")
        break

    else:
        print("Invalid choice")