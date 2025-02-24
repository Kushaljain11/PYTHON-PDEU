from collections import deque

queue = deque()

while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        element = input("Enter element: ")
        queue.append(element)
        print(f"{element} added to queue")

    elif choice == '2':
        if queue:
            print("Dequeued:", queue.popleft())
        else:
            print("Queue is empty")

    elif choice == '3':
        print("Queue:", list(queue))

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again.")
