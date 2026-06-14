# Ashley Stone
# 06/14/2026
# P1HW1
# This program uses math expressions with user input.

print("-----Calculating Exponents-----")

base = int(input("\nEnter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))

answer = base ** exponent

print("\n", base, "raised to the power of", exponent, "is", answer, "!!")
print("\n\n-----Addition and Subtraction-----")

start_num = int(input("\nEnter a starting integer: "))
add_num = int(input("Enter an integer to add: "))
subtract_num = int(input("Enter an integer to subtract: "))

total = start_num + add_num - subtract_num

print("\n", start_num, "+", add_num, "-", subtract_num, "is equal to", total)