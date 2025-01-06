# Program to unpack a sentence from input of user
# mrdthu003
# Maredi Thulani

wordlist = [] # creat a list to put values in
index = 0
# collect input from user in string form
sentence = input("Enter the coded sentence:\n")
#create a while loop to go through the input
while index <len(sentence):
    wordlength = int(sentence[index]) # take the first value of the sentece which is an integer
    word = sentence[index+1:index+wordlength+1] # take a word starting from after the integer in behind and stopping before the number of the second word
    wordlist.append(word) # put the collected words in a list created above
    index += wordlength + 1 # add to index until all the words a collected
# for loop to go through the list and print the words inside
for w in wordlist:
    print(w)
