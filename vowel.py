
def main():
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        word = input("Enter your word:\n").lower()
        f = open("vowels.txt", "a")
        if word != "q":
            for i in word:
                if i in vowel:
                    f.write(i)
            f.write("\n")
        else:
            break        
    f.close()
main()
