print("Employee Attendance and Salary Record System")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
days_worked = int(input("Enter number of days worked in a month: "))

daily_wage = 500
salary = days_worked * daily_wage

print("\nEmployee Details")
print("Name:", name)
print("Employee ID:", emp_id)
print("Days Worked:", days_worked)
print("Monthly Salary: Rs.", salary)
