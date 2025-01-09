"""21. Calculate net salary

where net salary = gross salary + allowance – deduction.

Allowances are 10% while deductions are 3% of gross salary"""

gross_salary=float(input("GROSS SALARY:"))
allowance=0.1*gross_salary
deduction=0.03*gross_salary

net_salary = gross_salary + allowance - deduction
print("THE NET SALARY IS:",net_salary)




