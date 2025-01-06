# Program to collect information from ID number
# mrdthu003
# Maredi Thulani

# take input of user in string form
ID = input("Please enter your ID number:\n")

# collect the numbers required to be analyzed
month = ID[2:4] 
year = ID[0:2]
day = ID[4:6]
# check the gender by satisfying the if statements
if "0000" <= ID[6:10] <= "4999":
    gender = "female."
else:
    gender = "male."
# check the citizenship by satisfying the if statements    
if ID[10] == "0":
    status = "South African citizen."
else: 
    status = "permanent resident."
# print the information collected in the reqired format    
print("Your date of birth is", day+"/"+month+"/"+year+".")
print("You are", gender)
print("You are a", status)
