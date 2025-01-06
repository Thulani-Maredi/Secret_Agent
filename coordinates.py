# Determining whether the inputed number form coordinates
# Thulani Maredi
# mrdthu003
# 01 March 2024

num1 = eval(input("Enter first number:\n"))
num2 = eval(input("Enter second number:\n"))
num3 = eval(input("Enter third number:\n"))
num4 = eval(input("Enter fourth number:\n"))
num5 = eval(input("Enter fifth number:\n"))
num6 = eval(input("Enter sixth number:\n"))

if -90<=num1<=90 and -180<=num4<=180 and 0<=num2<=59 and 0<=num5<=59 and 0<=num3<=59 and 0<=num6<=59:
    print("WOW! Looks like geographic coordinates!")
else: 
    print("Hmmm ... looks like 6 random numbers.")