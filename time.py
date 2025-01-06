# Checking if the time is valid
# Thulani Maredi
# MRDTHU003
# 26 February 2024

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

if (0<= hours and hours <=23) and (0<= minutes and minutes <=59) and (0<= seconds and seconds <=59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
