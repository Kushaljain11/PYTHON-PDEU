stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        element = input("Enter element: ")
        stack.append(element)
        print(f"{element} pushed to stack")

    elif choice == '2':
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")

    elif choice == '3':
        print("Stack:", stack)

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
