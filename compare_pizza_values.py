# This program will compare the price per square inch of two pizzas
import math

# User inputs the dimension and cost of the pizza
price1 = input("Enter the price of the first pizza in dollars: ")
diameter1 = input("Enter the diameter of the first pizza in inches: ")
price2 = input("Enter the price of the second pizza in dollars: ")
diameter2 = input("Enter the diameter of the second pizza in inches: ")

# Change the inputs from strings to integers
price1 = int(price1)
diameter1 = int(diameter1)
price2 = int(price2)
diameter2 = int(diameter2)

# Calculate area of each pizza
area1 = math.pi * (diameter1 / 2)**2
area2 = math.pi * (diameter2 / 2)**2

# Calculate the price per square inch of each pizza
value1 = area1 / price1
value2 = area2 / price2

# Round each value to two decimal places
value1 = round(value1, 2)
value2 = round(value2, 2)

# Print answer
print("The price per square inch of the first pizza is", value1)
print("The price per square inch of the second pizza is", value2)