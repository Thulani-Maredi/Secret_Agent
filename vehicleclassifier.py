# Program to classify the type of vehicle
# mrdthu003
# Maredi Thulani
# 04 May 2024

# Take input from user and convert from string to integer
GMV = int(input("What is the gross vehicle mass (in kg)?\n"))

# from the input check which weight class it falls into
if GMV <= 3500:
    # check if the vehicle has a trailer for all weight classes
    trailer = input("Does the vehicle have a trailer?\n")
    if trailer == "y":
        mass = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        # check the mass of the trailer and check if it satisfies the following if statement for all the weight classes then print the output
        if mass > 750:
            print("This vehicle is class EB.")
        else:
            print("This vehicle is class B.")
    # if it does not have a trailer check if it articulated the n print the output of the if statements for every weight class
    else:
        type = input("Is the vehicle articulated?\n")
        if type == "y":
            print("This vehicle is class EB.")
        else:
            print("This vehicle is class B.")
elif 3500 < GMV <= 16000:
    trailer = input("Does the vehicle have a trailer?\n")
    if trailer == "y":
        mass = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        if mass > 750:
            print("This vehicle is class EC1.")
        else:
            print("This vehicle is class C1.")
    else:
        type = input("Is the vehicle articulated?\n")
        if type == "y":
            print("This vehicle is class EC1.")
        else:
            print("This vehicle is class C1.")
else:
    trailer = input("Does the vehicle have a trailer?\n")
    if trailer == "y":
        mass = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
        if mass > 750:
            print("This vehicle is class EC.")
        else:
            print("This vehicle is class C.")
    else:
        type = input("Is the vehicle articulated?\n")
        if type == "y":
            print("This vehicle is class EC.")
        else:
            print("This vehicle is class C.")    