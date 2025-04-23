# Write a program to create a csv file that we can directly open in MS-Excel.
import csv

data = [
    ["Roll No", "Name", "Subject1", "Subject2", "Subject3"],
    [1, "Alice", 85, 78, 92],
    [2, "Bob", 90, 88, 79],
    [3, "Charlie", 75, 85, 89]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")
