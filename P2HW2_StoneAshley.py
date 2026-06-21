# Ashley Stone
# 06/14/2026
# P2HW2
# This program stores grades in a list and displays
# the lowest grade, highest grade, sum of grades,
# and average grade.

# Pseudocode:
# Ask user for Module 1 grade
# Ask user for Module 2 grade
# Ask user for Module 3 grade
# Ask user for Module 4 grade
# Ask user for Module 5 grade
# Ask user for Module 6 grade
# Store grades in a list
# Find lowest grade
# Find highest grade
# Find sum of grades
# Find average grade
# Display results

# Enter grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Create list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculate results
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Display results
print("\n------------Results------------")

print(f"Lowest Grade:      {lowest}")
print(f"Highest Grade:     {highest}")
print(f"Sum of Grades:     {total}")
print(f"Average:           {average:.2f}")

print("--------------------------------")   