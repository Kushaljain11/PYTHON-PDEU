# o	Write a program that receives an integer an input. If a string is entered instead of an integer, 
# then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied.


while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"You entered the integer: {user_input}")
        break
    except ValueError:
        print("Error: That's not an integer. Please try again.")
