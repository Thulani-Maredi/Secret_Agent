import string

def palindrome (s):
   # change base case to make code run efficiently
   if len(s) == 0:
      return True
   elif s[0] in string.punctuation or s[0] in string.whitespace:
      return palindrome(s[1:]) # fix the slicing to start from 2nd letter not last
   elif s[-1] in string.punctuation or s[-1] in string.whitespace:
      return palindrome(s[:-1])
   elif s[0].lower() == s[-1].lower():
      return palindrome(s[1:-1])
   else:
      return False