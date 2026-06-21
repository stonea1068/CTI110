# Ashley Stone
# 06/14/2026
# P2LAB2
# This program uses a dictionary to store vehicle MPG values
# and calculates the gallons of gas needed for a trip.

# Create dictionary
vehicles = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Store keys in a variable
keys = vehicles.keys()

# Display vehicle options
print(keys)

# Ask user for vehicle
vehicle = input("\nEnter a vehicle to see its mpg: ")

# Display MPG
print(f"\nThe {vehicle} gets {vehicles[vehicle]} mpg.")

# Ask for miles driven
miles = float(input("\nHow many miles will you drive? "))

# Calculate gallons needed
gallons = miles / vehicles[vehicle]

# Display gallons needed
print(f"\n{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.0f} miles.")