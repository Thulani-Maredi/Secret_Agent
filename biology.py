# Program to identify the type of animal
# Thulani Maredi
# MRDTHU003
# 29 February 2024

print("Welcome to the Biology Expert")
print("-----------------------------")
print("Answer the following questions by selecting from among the options.")

skeleton = input("The skeleton is (internal/external)?\n") 
if skeleton == "internal": # Continue with questions if internal is chosen
    eggs = input("The fertilisation of eggs occurs (within the body/outside the body)?\n") 
    if eggs == "within the body":
        young = input("Young are produced by (waterproof eggs/live birth)?\n")
        if young == "waterproof eggs":
            skin = input("The skin is covered by (scales/feathers)?\n")
            if skin == "scales": 
                print("Type of animal: Reptile")
            else: 
                print("Type of animal: Bird")
        else: 
            print("Type of animal: Mammal")
    else:
        lives =input("It lives (in water/near water)?\n") 
        if lives == "in water": # If outside of the body is choosen then it will ask if the whether it live in or near water
            print("Type of animal: Fish")
        else:
            print("Type of animal: Amphibian")
else: # If something other than internal is chosen in this case external
    print("Type of animal: Arthropod")