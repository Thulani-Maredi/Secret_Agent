# Writing  a personlised spam message
# Thulani Maredi
# MRDTHU003
# 26 February 2024

name = input("Enter first name:\n")
surname = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")

stringmoney = str(money)
percent = str( money*30/100)

print("\nDearest "+ name +"\nIt is with a heavy heart that I inform you of the death of my father,\nGeneral Fayk " + surname +", your long lost relative from Mapsfostol.\nMy father left the sum of "+ stringmoney +"USD for us, your distant cousins.\nUnfortunately, we cannot access the money as it is in a bank in "+ country +".\nI desperately need your assistance to access this money.\nI will even pay you generously, 30% of the amount - "+ percent +"USD,\nfor your help.  Please get in touch with me at this email address asap.\nYours sincerely\nFrank "+ surname)