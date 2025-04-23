# 3. Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
employees = [
    {"dept": "HR", "roll_no": 101, "salary": 50000},
    {"dept": "IT", "roll_no": 102, "salary": 70000},
    {"dept": "HR", "roll_no": 103, "salary": 60000},
    {"dept": "IT", "roll_no": 104, "salary": 80000},
    {"dept": "Sales", "roll_no": 105, "salary": 45000}
]
from collections import defaultdict
dept_salaries = defaultdict(list)
for emp in employees:
    dept_salaries[emp["dept"]].append(emp["salary"])
for dept, salaries in dept_salaries.items():
    print(dept, min(salaries), max(salaries))
