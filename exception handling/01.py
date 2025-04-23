while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"You entered the integer: {user_input}")
        break
    except ValueError:
        print("Error: That's not an integer. Please try again.")
