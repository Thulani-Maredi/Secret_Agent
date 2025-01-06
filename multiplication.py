# program to give out the multiples of numbers
# mrdthu003
# Maredi Thulani
# 06 May 2024

# Take input from user
num = input("Enter a value for n (not greater than 30):\n")

# check if string is made up of integers
if num.isdigit():
    num = int(num) # convert the string into integer
    if num>30 or num <1: # check if it satisfies the if statement
        print("Sorry, n must be an integer number in the range 1 to 30.")
    else:
         
        print("Table from", str(num), "to", str(num+10) + ":")
        # print the first row of the table
        print("*  |", end= "")
        for i in range(num,num+10): # a loop of all 10 the numbers after the given number
            print('{0:>4}'.format(i), end="")
        print()
        print('{0:-^44}'.format("-")) # print the lines under the first row
        # printing the first column of the table
        for i in range(num,num+10):
            if i >= 10:
                print(i,"|",end='') # if the numbers are greater than 10 the print | sign with no spaces
            else:
                print(i," |",end='') # else put a space befor the | sign if its below 10
            # create a for loop to multiply the values in the graph and put them in order    
            for p in range(num,num+10):
                print('{0:>4}'.format(p*i),end = '')
            print()
                
            
else:
    print("Sorry, n must be an integer number in the range 1 to 30.")
        
    
    
