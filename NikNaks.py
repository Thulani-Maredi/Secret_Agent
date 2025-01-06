# Program to guess correct letters of a word
# mrdthu003
# 25 July 2024

def main():
 # Take difficulty from user and print range of words
 print("Guess the mystery 4 letter code. (No letter occurs more than once.)")
 limit = int(input("Choose difficulty level (4 to 26):\n"))
 letters=list('abcdefghijklmnopqrstuvwxyz')[0: limit]
 print('The letters in the code are chosen from: {}.'.format(letters))
 
 # Generate a secret code for the game
 import random 
 secret_code=[]
 
 for i in range(4):
    rand_index = random.randint(0, len(letters)-1)
    letter = letters.pop(rand_index)
    secret_code.append(letter)
 print(secret_code)
 # Limit player input to only 10 guesses
 guesses = 10
 while guesses > 0:
    print("You have "+str(guesses)+" guesses remaining.")
    guess = input("Enter your guess:\n")
    
    # Determining the niks and naks by uing a loop to go through the secret code
    niks = 0
    naks = 0
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            niks += 1
        elif guess[i] in secret_code:
            naks += 1

    # print out the results after player input
    if niks == 4:
        print("Correct!")
        break
    else:
     if (niks > 1 or niks == 0) and (naks > 1 or naks == 0):
        print("There are "+str(niks)+" Niks and "+str(naks)+" Naks.")
     elif niks == 1 and naks == 1:
      print("There is "+str(niks)+" Nik and "+str(naks)+" Nak.")
     elif niks == 1 and (naks > 1 or naks == 0):
      print("There is "+str(niks)+" Nik and "+str(naks)+" Naks.")
     elif (niks > 1 or niks == 0) and naks == 1:
      print("There are "+str(niks)+" Niks and "+str(naks)+" Nak.")
    guesses = guesses -1
    
 # Outcome if user runs out of guesses
 code = "".join(secret_code)
 if guesses == 0:
    print("Sorry, you lose.")
    print("The secret number was "+code+".")  
 
if __name__ == "__main__":
 main()