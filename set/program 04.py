def remove_substring(onestring, removestring):
    # Check if the remove_string is present in the onestring
    if removestring in onestring:
        # Remove the remove_string from the onestring
        onestring = onestring.replace(removestring, "")
    return onestring

# Example usage
onestring = input("Enter the original string: ")
removestring = input("Enter the string to remove: ")

# Call the function and print the result
final_string = remove_substring(onestring, removestring)
print("The final string is:", final_string)
