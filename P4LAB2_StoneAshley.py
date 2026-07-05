# Ashley Stone
# 07/05/2026
# P4LAB2
# This program uses loops to display a multiplication table.

# Start program again variable

run_again = "yes"

# While loop controls repeating program

while run_again == "yes":

    # Ask user for integer
    number = int(input("\nEnter an integer: "))

    # Check for negative number
    if number < 0:
        print("\nThis program does not handle negative numbers!")

    else:
        # For loop displays multiplication table
        for count in range(1, 13):
            answer = number * count
            print(f"{number} * {count} = {answer}")

    # Ask user if they want to run again
    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program...")