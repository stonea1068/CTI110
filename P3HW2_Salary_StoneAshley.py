# Ashley Stone
# 07/04/2026
# P3HW2 Salary
# This program calculates an employee's regular pay,
# overtime pay, and gross pay.

# Pseudocode:
# Ask user to enter employee name
# Ask user to enter hours worked
# Ask user to enter pay rate
# If hours worked is more than 40
#     Calculate overtime hours
#     Calculate overtime pay at 1.5 times pay rate
#     Calculate regular pay for 40 hours
# Else
#     Overtime hours equals 0
#     Overtime pay equals 0
#     Calculate regular pay for hours worked
# Calculate gross pay
# Display employee name, pay rate, hours worked,
# overtime hours, overtime pay, regular pay, and gross pay

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

gross_pay = regular_pay + overtime_pay

print("-------------------------------------")
print("Employee name:", employee_name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("------------------------------------------------------------------------------------------------")
print(f"{hours_worked:<15.1f}{pay_rate:<15.2f}{overtime_hours:<15.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")