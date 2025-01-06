def main():
    while True:
        line = input("Enter bar length or enter q to quit:\n")
        f = open("numbers.txt", "a")
        if line.isdigit():
            line = int(line)
            print("*" * line, file = f)
        else:
            break
        f.close()
main()