# Program to print 7 numbers starting starting from that number
# Thulani Maredi 
# mrdthu003
# 08 March 2024

num1 = int(input("Enter a number between -6 and 2:\n"))

count = num1



if -6 <= num1 <= 2:
 for i in range(num1,num1+6):
  for l in range(7):
    print(format (count,(">2")), end = ' ')
    count += 1
  print()

else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")

