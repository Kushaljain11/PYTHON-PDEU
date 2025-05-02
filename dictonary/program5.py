# 5. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased.
# By using the values from these two dictionaries compute the total bill.
prices = {'milk': 40, 'bread': 30, 'eggs': 10}
quantities = {'milk': 2, 'bread': 1, 'eggs': 12}
total_bill = 0
for item in prices:
    total_bill += prices[item] * quantities.get(item, 0)
print(total_bill)
