# Program to print 7 numbers starting starting from that number
# Thulani Maredi 
# mrdthu003
# 08 March 2024

num1 = int(input("Enter a number between -6 and 93:\n"))

count = 0



if -6 <= num1 <= 93:
 for i in range(num1,num1+7):
    print(format (i,(">2")), end = ' ')
    count += 1

else:
    print("Invalid input! The value of 'n' should be between -6 and 93.")

