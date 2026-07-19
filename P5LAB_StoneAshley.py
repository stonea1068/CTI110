# Ashley Stone
# 07/19/2026
# P5LAB
# This program simulates a self-checkout machine by generating
# a random purchase total, accepting payment, and dispensing change.

import random


# Function to calculate and display change
def disperse_change(change):

    cents = int(round(change * 100))

    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents

    print("\nChange is:")

    if dollars == 1:
        print("1 Dollar")
    elif dollars > 1:
        print(f"{dollars} Dollars")

    if quarters == 1:
        print("1 Quarter")
    elif quarters > 1:
        print(f"{quarters} Quarters")

    if dimes == 1:
        print("1 Dime")
    elif dimes > 1:
        print(f"{dimes} Dimes")

    if nickels == 1:
        print("1 Nickel")
    elif nickels > 1:
        print(f"{nickels} Nickels")

    if pennies == 1:
        print("1 Penny")
    elif pennies > 1:
        print(f"{pennies} Pennies")


# Main function
def main():

    # Generate random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${amount_owed:.2f}")

    cash = float(input("How much cash will you put in the self-checkout? $"))

    change = cash - amount_owed

    print(f"\nChange owed: ${change:.2f}")

    disperse_change(change)


# Call main function
main()