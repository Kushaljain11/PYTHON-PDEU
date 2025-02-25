# Create an empty set
names_set = set()

# Add five names to the set
names_set.update(["Alice", "Bob", "Charlie", "David", "Eva"])

# Modify one name (remove "Charlie" and add "Charles")
names_set.remove("Charlie")
names_set.add("Charles")

# Delete two names from the set
names_set.discard("Alice")
names_set.discard("Bob")

# Display the updated set
print("Updated names set:", names_set)
