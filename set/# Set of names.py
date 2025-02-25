# Set of names
names = {"Alice", "Bob", "Alex", "Brian", "Blake", "Charlie", "David"}

# Separate names starting with A and B
names_starting_with_A = {name for name in names if name.startswith('A')}
names_starting_with_B = {name for name in names if name.startswith('B')}

# Display the two sets
print("Names starting with A:", names_starting_with_A)
print("Names starting with B:", names_starting_with_B)
