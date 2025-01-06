earn = float(input("Enter amount earned:\n"))
org = input("Enter charity organisation(enter na if not applicable):\n")

if earn <= 36000 :
    print("Amount earned is", earn)
elif 36000 <= earn <= 72000 and org == "government":
    tax = earn*(15/100)
    earn1 = earn - tax
    print("Amount earned is", earn1)
elif 36000 <= earn <= 72000 and org == "company":
    tax = earn*(20/100)
    earn1 = earn - tax
    print("Amount earned is", earn1)
else:
    tax = earn*(25/100)
    earn1 = earn - tax
    print("Amount earned is", earn1)    
    
    