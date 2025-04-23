# Read the data stored in MS-Excel file and convert it into a dictionary.
import csv

data_dict = {}
with open("students.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = row["Roll No"]
        total = int(row["Subject1"]) + int(row["Subject2"]) + int(row["Subject3"])
        data_dict[rollno] = {
            "name": row["Name"],
            "marks": [int(row["Subject1"]), int(row["Subject2"]), int(row["Subject3"])],
            "total": total
        }

print("Dictionary Data:")
for k, v in data_dict.items():
    print(k, ":", v)
