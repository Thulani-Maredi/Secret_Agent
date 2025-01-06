# Program to comment if ID number is valid or not
# mrdthu003
# Maredi Thulani
# 9 may 2024

# collect value of ID from the user
ID = input("Please enter your ID number:\n")

# from ID take all the evenly numbered values
ID3 = ID[:13:2] 
# from ID take all the oddly numbered values
ID2 = ID[1:12:2] 
# from the evenly numbered valuesconvert them into integers multiply them by two and if they are bigger than 9 subtract 9 from them.
n1 = int(ID2[0])
nn1 = n1*2
if nn1 >9:
    nn1 = nn1 -9
n2 = int(ID2[1])
nn2 = n2*2
if nn2 >9:
    nn2 = nn2 -9
n3 = int(ID2[2])
nn3 = n3*2
if nn3 >9:
    nn3 = nn3 -9
n4 = int(ID2[3])
nn4 = n4*2
if nn4 >9:
    nn4 = nn4 -9
n5 = int(ID2[4])
nn5 = n5*2
if nn5 >9:
    nn5 = nn5 -9 
n6 = int(ID2[5])
nn6 = n6*2
if nn6 >9:
    nn6 = nn6 -9 
    
# Add all the ID numbers excluding the last digit then take the sum modulus 10 and subtract them from 10
sum = int(ID3[0])+nn1+int(ID3[1])+nn2+int(ID3[2])+nn3+int(ID3[3])+nn4+int(ID3[4])+nn5+int(ID3[5])+nn6
sum2 = 10 - (sum%10)

# if the the sum2 is equal to the last digit of the ID then print out informaion about the ID number
if sum2 == int(ID[12]):
    year = ID[0:2]
    month = ID[2:4]
    day = ID[4:6]
    
    if "0000" <= ID[6:10] <= "4999":
        gender = "female."
    else:
        gender = "male."
        
    if ID[10] == "0":
        status = "South African citizen."
    else: 
        status = "permanent resident."
        
    print("Your date of birth is", day+"/"+month+"/"+year+".")
    print("You are", gender)
    print("You are a", status)
else:
    print("Invalid ID number.")



