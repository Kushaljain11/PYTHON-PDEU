my_tuple = (1, 2, 3, 4)

# Convert to list, delete element, then convert back to tuple
temp_list = list(my_tuple)
temp_list.remove(3)
new_tuple = tuple(temp_list)

print("Tuple after deleting element:", new_tuple)
