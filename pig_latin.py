# Program to translate to pig latin
# Maredi Thulani
# mrdthu003
# 21 March 2024

sentence = input("Enter a sentence:\n")
sentence = sentence.lower() # turn the sentence into lower case 
words = sentence.split() # split the sentence into a list of words 
vowels = ['a','e','i','o','u']

for word in words: # search for all the word in the list of words 
    finalIndex = 1000000 
    if word[0] in vowels: # search for the first letter of each word and check if it has a vowel
        print(word +'way', end=" ") # add way to the words that start with a vowel
    else:
        for vowel in vowels: # go through the list of vowels 
            index = word.find(vowel) # find the first the position of the first vowel in the word 
            if (index!=-1 and index < finalIndex): # if found no vowels and the isn't a vowel in the first 1000000 letters of the word 
                finalIndex = index
        if (finalIndex ==1000000): # if no vowel is found in the word
            print("a"+word+"ay", end=" ") # print a then the word itself then ay
        else:
            print(word[finalIndex:]+"a"+word[0:finalIndex]+"ay", end=" ") # print the the word starting from the first vowel in the word an place it in front of the word then place a then constinants found the ay 
        
            
        
       