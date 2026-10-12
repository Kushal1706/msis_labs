capacity=5
stack=[None]*capacity
top = -1

def push(stack, data,top):
    if top == capacity-1:
        print("stack overflow")
        return top
    top += 1
    stack[top] = data
    return top

def pop(stack,top):
    if top == -1:
        print("Stack Underflow")
        return top
    value = stack[top]
    stack[top]=None
    top -=1
    print("Poped ele:",value)
    return top


def peek(stack,top):
    if top == -1:
        print("Stack is empty")
        return
    print("Top ele:",stack[top])


def isEmpty():
    return top == -1


def isFull():
    return top == capacity-1

def display(stack,top):
    if top==-1:
        print("Stack is empty")
    else:
        print("Stack ele from top to bottom:\n")
        for i in range(top, -1, -1):
            print(stack[i])


while True:
    print("\n===== STACK USING PYTHON LIST =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Check if Empty")
    print("5. Check if full")
    print("6. Display")
    print("7. Exit")

    choice = input("enter your choice")

    if choice == "1":
        data = int(input("Enter the ele:"))
        top=push(stack, data,top)
    elif choice == "2":
        top=pop(stack,top)
    elif choice == "3":
        peek(stack,top)
    elif choice == "4":
        print(isEmpty())
    elif choice == "5":
        print(isFull())
    elif choice == "6":
        top=display(stack,top)
    elif choice == "7":
        print("Program terminated")
        break
    else:
        print("Invalid choice")
