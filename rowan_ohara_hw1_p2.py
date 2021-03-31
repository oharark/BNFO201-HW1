# This program will calculate how many T4 phages tall someone is

# User inputs number of inches tall they are
inches = input("Enter your height in inches: ")
inches = eval(inches)

# Convert inches to centimenters
centimeters = inches * 2.54

# Convert centimeters to milimeters
milimeters = centimeters * 10

# Convert milimeters to nanometers
nanometers = milimeters * 10**6

# Calculate how many T4 phages tall someone is
phages = nanometers/200

# Print answer
print("You are", phages, "phages tall.")