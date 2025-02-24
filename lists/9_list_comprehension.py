list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [4, 5, 6, 7, 8, 9, 10]

unique_list = [x for x in list1 if x not in list2]

print("Numbers in list1 but not in list2:", unique_list)
