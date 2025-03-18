def sanitize_list(lst):
    if not lst:
        return []
    if lst[0] < 0:
        return [0] + sanitize_list(lst[1:])
    return [lst[0]] + sanitize_list(lst[1:])

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"Sanitized list: {sanitize_list(numbers)}")
