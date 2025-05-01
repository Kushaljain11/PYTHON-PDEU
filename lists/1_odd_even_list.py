#  1.	Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos.
# Replace the third element of odd integers with  a list of 4 even integers.
# Flattern, sort and print the list. Provide appropriate message at each stage.

import random

odd_list = random.sample(range(1, 100, 2), 5)
even_list = random.sample(range(2, 100, 2), 4)

print("Initial Odd List:", odd_list)
print("Initial Even List:", even_list)

odd_list[2:3] = even_list

flattened_sorted_list = sorted(odd_list)
print("Flattened and Sorted List:", flattened_sorted_list)
