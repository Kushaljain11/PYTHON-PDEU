names = ["Alice", ("John",), "Emma", ("Mike",), "Sophia", ("David",)]
boy_count = sum(1 for name in names if isinstance(name, tuple))
girl_count = len(names) - boy_count

print("Number of Boys:", boy_count)
print("Number of Girls:", girl_count)
