# Program to put info on a credit card
# Maredi Thulani
# mrdthu003
# 23 April 2024

name = input("Enter the card holder's name:\n")

# Take the credit card number of 16 digits then create spaces between every 4 digits
card_number = input("Enter the 16 digit card number (no spaces please):\n")
card_number2 = card_number[0:4]+" "+card_number[4:8]+" "+card_number[8:12]+" "+card_number[12:16]

# Take the issue date then replace the ":" symbol with the "/" symbol between the digits
issue_date = input("Enter the date of issue (mm:yy):\n")
issue_date2 = str(issue_date[:2])+"/"+str(issue_date[3:])

# Take the expiry date then replace the ":" symbol with the "/" symbol between the digits
expiry_date = input("Enter the expiry date (mm:yy):\n")
expiry_date2 = str(expiry_date[:2])+"/"+str(expiry_date[3:])
 

code = int(input("Enter the 3 digit security code:\n"))

# Take the credit limit then round offf to the nearest 2 decimals
limit = float(input("Enter the credit limit (Rand):\n"))
limit1 = "%.2f"%limit

# Take the balance then round offf to the nearest 2 decimals
balance = float(input("Enter the balance (Rand):\n"))

balance1 = "%.2f"%balance 

# Calculate the available balance by subtracting re balance from the limit then round off the amount to the nearest 2 decimal spaces
available = limit - balance
available1 = "%.2f"%available
print("")

# print the format of the credit card
print("+------------- Credit Card Account --------------+")
print(f"| Card holder:   {name}".ljust(48),"|")
print(f"| Card number:   {card_number2}".ljust(48),"|")
print(f"| Date of issue: {issue_date2}    Expiry date: {expiry_date2}".ljust(48),"|")
print(f"| Security code: {code}".ljust(48),"|")
print(f"| Credit limit:  {limit1} Rand".ljust(48),"|")
print(f"| Available:     {available1} Rand".ljust(48),"|")
print(f"| Balance:       {balance1} Rand".ljust(48),"|")
print("+------------------------------------------------+")