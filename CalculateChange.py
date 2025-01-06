# program to determine how ,any R5, R2 and R1 coins are in a certain amount of money
# Maredi Thulani
# mrdthu003
# 9 April 2024

amount = int(input("Enter change amount:\n"))

a = amount // 5
a1 = amount % 5
b = a1 // 2
b1 = a1 % 2 
c = b1 //1 

print("The change:",str(a)+" R5 coins",str(b)+" R2 coins",str(c)+" R1 coins", sep = '\n')