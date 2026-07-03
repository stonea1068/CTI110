# Ashley Stone
# 07/03/2026
# P3LAB
# This program calculates the fewest number of dollars and coins
# needed to make a given amount of money.

# Get amount from user
money = float(input("Enter the amount of money as a float: $"))

# Convert dollars to cents
cents = int(money * 100)

# Calculate dollars and coins
dollars = cents // 100
cents = cents - (dollars * 100)

quarters = cents // 25
cents = cents - (quarters * 25)

dimes = cents // 10
cents = cents - (dimes * 10)

nickels = cents // 5
cents = cents - (nickels * 5)

pennies = cents

# Display results
print("\nThe money is:")

# Dollars
if dollars == 1:
    print("1 Dollar")
elif dollars > 1:
    print(f"{dollars} Dollars")

# Quarters
if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(f"{quarters} Quarters")

# Dimes
if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(f"{dimes} Dimes")

# Nickels
if nickels == 1:
    print("1 Nickel")
elif nickels > 1:
    print(f"{nickels} Nickels")

# Pennies
if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(f"{pennies} Pennies")