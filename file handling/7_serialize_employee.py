# Write a program to serialize and deserialize Employee object with empcode, empname, Date of Joining, Salary
import pickle

class Employee:
    def __init__(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"{self.code}, {self.name}, {self.doj}, {self.salary}"

emp = Employee("E001", "John Doe", "2023-01-15", 50000)

with open("employee.dat", "wb") as f:
    pickle.dump(emp, f)

with open("employee.dat", "rb") as f:
    loaded_emp = pickle.load(f)

print("Deserialized Employee:")
print(loaded_emp)
