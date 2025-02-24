tuples_list = [(), (1, 2), (), (3, 4), (), (5,)]
filtered_list = [t for t in tuples_list if t]

print("List after removing empty tuples:", filtered_list)
