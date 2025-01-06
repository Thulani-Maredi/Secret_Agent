# create a program to check if two words are the same
# mrdthu003
# 01 September 2024

def equals(word_one,word_two):
    # check if all the values in both variables are exhausted then return true
    if len(word_one) == 0 and len(word_two) == 0:
        return True
    # check if either value in one variable is exhausted and the other isn't then return true
    if len(word_one) == 0 or len(word_two) == 0:
        return False  
    # check if the two strings share the same first letter, do so until exhausted, the repeat for all letters
    elif word_one[0].lower() == word_two[0].lower():
        return equals(word_one[1:],word_two[1:])
    else:
        return False
    
def query(pattern, word):
    # If the the lengths of the two words are not the same return false
    if len(pattern) != len(word):
        return False
    # check if all the values in both variables are exhausted then return true
    elif len(pattern) == 0 and len(word) == 0:
        return True
    # if the fist letters in each word are the same or if the word in pattern contains ?, check the next letters in both words until exhausted
    elif pattern[0] == word[0] or pattern[0] == "?":
        return query(pattern[1:], word[1:])
    else:
        return False
    
def match(pattern, word):
    # check if the letters of only the pattern is exhausted as your base case to return true because the difference of length does not matter 
    if len(pattern) == 0:
        return True
    # return * in pattern if string of word is exhasted to make it True for match
    elif len(word) == 0:
        return pattern == "*"
    # check for * in 1st index to change either the pattern or word
    elif pattern[0] == "*":
        return match(pattern[1:], word) or match(pattern, word[1:])
    # check for same letter in 1st index or ? in 1st index pattern
    elif pattern[0] == word[0] or pattern[0] == "?":
        return match(pattern[1:], word[1:])    
    else: 
        return False
    
