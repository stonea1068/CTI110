# Ashley Stone
# 06/14/2026
# P1HW2
# This program calculates and displays travel expenses.

# Pseudocode:
# Ask user to enter budget
# Ask user to enter travel destination
# Ask user to enter gas expense
# Ask user to enter accommodation expense
# Ask user to enter food expense
# Add all expenses together
# Subtract expenses from budget
# Display travel expense summary

print("This program calculates and displays travel expenses")


budget = float(input("\nEnter your budget: "))
destination = input("\nEnter your travel destination: ")
gas_expense = float(input("\nEnter your gas expense: "))
accommodation_expense = float(input("\nEnter your accommodation expense: "))
food_expense = float(input("\nEnter your food expense: "))

total_expenses = gas_expense + accommodation_expense + food_expense
remaining_budget = budget - total_expenses

print("\n-----Travel Expense Summary-----")
print("Destination:", destination)
print("Budget:", budget)
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)
