food_items = [("Pizza", 12), ("Burger", 8), ("Pasta", 10), ("Salad", 6)]

sorted_food = sorted(food_items, key=lambda x: x[1], reverse=True)
print("Sorted Food Items by Price (Descending):", sorted_food)
