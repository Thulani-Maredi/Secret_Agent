# program to interact with user
# Maredi Thulani 
# mrdthu003
# 18 April 2024

# Introduce self then collect information from the user 
print("Hello, I am Eugene Junior.")
name = input("What is your first name?\n")
surname = input("What is your last name?\n")
title = input("And what is your preferred title?\n")
# print the greetings 
print("Hi",title,name[0]+".",surname+"!")

# Collect Course information frm the user
course = input("What is the course code of your current course?\n")
# Ask what the course code stands for
course2 = input("So, what does '"+course[0:3]+"' stand for?\n")
# print final statement for course information
print(course2,"sounds interesting.")

# Take weight of user in kilograms and convert it to pounds and ounces
w = float(input("What weight are you in kilograms?\n"))
ounces = (w*1000)/28.35 
pounds = int(ounces/16)
ounces2 = round(ounces) % 16
print("That's", pounds,"lbs and", ounces2,"ounces in the US!")

# collect date of birth and year then calculate current age and print the age 
date = input("What's today's date (dd/mm/yy)?\n")
birth = int(input("And what year were you born?\n"))
age = "20" + date[6:]
age2 = int(age) - birth
print("Okay, so you're", age2, "this year.")
print("Nice talking to you, bye!")


 

