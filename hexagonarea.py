# Program to calculate the are of a hexagon
# MAredi Thulani 
# mrdthu001
# 22 April 2024


import math # import the math file
length = eval(input("Enter the length of the side (cm):\n")) # Collect length from the user
area = (3*math.sqrt(3))/2*(length**2) # Calculate the are using the squre root function from the maths file
area_rounded = "%.3f"%area # Round off the answer to the nearest 3 decimals
print("The area of a hexagon of side",length, "is", area_rounded+".") 