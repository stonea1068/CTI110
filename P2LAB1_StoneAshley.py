# Ashley Stone
# 06/14/2026
# P2LAB1
# This program calculates the diameter, circumference,
# and area of a circle using a radius entered by the user.

import math

# Get radius from user
radius = float(input("Enter the radius of the circle: "))

# Calculate circle measurements
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display results
print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"The circumference of the circle is {circumference:.2f}")
print(f"The area of the circle is {area:.3f}")