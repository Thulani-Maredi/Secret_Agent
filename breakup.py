# Creating a list of different words
# Maredi thulani
# mrdthu003
# 21 march 2024

word = input("Enter a sentence:\n")

vol = word.lower() # makes all words in sentence lower case
store = vol.split() # make a list of every word in sentence
print("The word list: ", end ='')
words = '' # make empty space for repeated words to form base on
for n in store: # use for loop to search or each word in list
 words = words + n+', ' # puts out the words in the loops then places comma after each word
 
print(words[0:len(words)-2], end ='.') # print out the words but slice out the comma at the end of the final word to replace with a comma