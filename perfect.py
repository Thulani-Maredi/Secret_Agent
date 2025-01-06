# Program to determine the perfect number
# Thulani Maredi 
# mrdthu003
# 01 March 2024


num1 = eval(input("Enter a number:\n"))
print("The proper divisors of",num1, "are:\n" )
count = 0

for i in range(1,num1,):
 if num1%i==0:
  print(i, end=' ')
  count +=i
  
 
if count==num1 :
 print("\n")
 print(num1,"is a perfect number.")
else: 
 print("\n")
 print(num1,"is not a perfect number.")