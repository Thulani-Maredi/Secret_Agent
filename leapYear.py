# Determining whether a year is a leap year
# Thulani Maredi
# MRDTHU003
# 26 February 2024

year = eval(input("Enter a year:\n"))
if year%400==0:
 print(str(year) + " is a leap year.")
elif year%4== 0 and year%100 >0:
 print(str(year) + " is a leap year.")
else:
  print(str(year) + " is not a leap year.")