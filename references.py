# Program to fix the inputed reference 
# Maredi Thulani
# mrdthu003
# 26 March 2024


reference = input("Enter the reference:\n")

names = reference.find('(')+1 # find the position of the first open bracket
part1 = reference[0:names].title() # make the first letters of each word at the start to the first open bracket a capital letter
year = reference.find(')') # find the position of the closed bracket
part2 = reference[names:year+1] # take the characters and including the open and closed bracket
topic = reference.find(',', names) # find the position of the first comma in the reference
part3 = reference[year+2:topic].capitalize() # capitalize the first letter of the word of the sentence before the comma and after the closed bracket
rest = reference[topic:] # print the rest of the remaining reference after the first comma

print('Reformatted reference:\n'+part1+part2+' '+part3+rest)