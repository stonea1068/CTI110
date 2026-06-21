# Ashley Stone
# 06/14/2026
# P2HW1
# This program calculates and displays travel expenses
# using formatted output.

print("This program calculates and displays travel expenses")

# Get user input
budget = float(input("\nEnter Budget: "))

destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))

hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))

food = float(input("\nLast, how much do you need for food? "))

# Calculate expenses
expenses = gas + hotel + food
remaining_balance = budget - expenses

# Display formatted results
print("\n------------Travel Expenses------------")

print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'Fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${hotel:.2f}")
print(f"{'Food:':20}${food:.2f}")

print("---------------------------------------")

print(f"\n{'Remaining Balance:':20}${remaining_balance:.2f}")