def average(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if lst else 0
    
    return average(lst, index + 1, total + lst[index])
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Average of the numbers: {average(numbers)}")
