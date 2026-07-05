# Ashley Stone
# 07/05/2026
# P4HW2
# This program calculates salary information for multiple employees
# using loops and decision structures.

# Pseudocode:
# Create variables to store totals
# Ask user to enter employee name
# While employee name is not Done
#     Ask user for hours worked
#     Ask user for pay rate
#     If hours are greater than 40
#         Calculate overtime hours
#         Calculate overtime pay
#         Calculate regular pay
#     Else
#         Overtime hours equals 0
#         Overtime pay equals 0
#         Calculate regular pay
#     Calculate gross pay
#     Add values to totals
#     Display employee pay information
#     Ask for next employee name
# Display total employees and all pay totals


# Starting totals

total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0


# Ask first employee

employee_name = input('Enter employee\'s name or "Done" to terminate: ')


# Loop until Done

while employee_name != "Done":

    hours = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate

    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * pay_rate


    gross_pay = regular_pay + overtime_pay


    total_employees += 1
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay


    print()
    print("Employee name:", employee_name)
    print()

    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay'}")
    print("--------------------------------------------------------------------------------------------")

    print(f"{hours:<15.1f}{pay_rate:<15.2f}{overtime_hours:<15.1f}{overtime_pay:<18.2f}${regular_pay:<17.2f}${gross_pay:.2f}")

    print()

    employee_name = input('Enter employee\'s name or "Done" to terminate: ')


# Final totals

print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")