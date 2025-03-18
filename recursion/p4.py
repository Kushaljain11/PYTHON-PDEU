def reverse_list(lst):
    
    if len(lst) <= 1:
        return lst
    
    
    return reverse_list(lst[1:]) + [lst[0]]


numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Reversed list: {reverse_list(numbers)}")
