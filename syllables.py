# Given a word, calculate how many syllables it contains.
# Thulani Maredi
# mrdthu003
# 01 April 2024



def count_syllables(word):
    count = 0
    for c in word:
        if c =='a' or c =='e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
            A = word.find('a')
            E = word.find('e')
            O = word.find('o')
            U = word.find('u')
            I = word.find('i')
            print(A,E,O,I,U)
        else:
            print("")
    return A,E,O,I,U
    

def main():
    word = input('Enter a word (or \'q\' to quit):\n')
    


if __name__ == '__main__':
    main()
    
 