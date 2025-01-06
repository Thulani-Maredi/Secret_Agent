# program to read words and return location of words
# mrdthu003
# 19 September 2024


# Reads the book and finds where each word is located
def read_book(filename):
    book_words = {} # store words and position
    # open the file and read
    with open(filename, 'r', encoding='utf-8') as file:
        # iterate through each line of book
        for line_num, line in enumerate(file, start=1):
            words = line.strip().split()
            for word_index, word in enumerate(words, start=1):# go throgh word in line
            
                cleaned_word = word.strip('?!.,;:)([]{}\'" \n').lower()
                if cleaned_word not in book_words: # if word not in dictionary
                    book_words[cleaned_word] = []
                book_words[cleaned_word].append(f"{line_num}-{word_index}")
    return book_words # return dictionary with words and position

# Encodes the message using the positions of the words in the book
def encode_message(book_words, message):
    encoded_message = ["BEGIN"] # start the mesage at bigin
    for word in message.split():
        clean = word.strip('?!.,;:)([]{}\'" \n').lower()
        if clean in book_words: # if word in book
            encoded_message.append(book_words[clean][0])
        else:
            encoded_message.append(word)
    encoded_message.append("END")
    return encoded_message

# Writes the encoded message to a file and prints it
def write_output(filename, encoded_message):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in encoded_message:
            file.write(line + "\n")
    for line in encoded_message:
        print(line)

# Main function to run the program
def main():
    book_filename = input("Enter the book filename:\n")
    message = input("Enter the message:\n")
    output_filename = input("Enter the output filename:\n")

    book_words = read_book(book_filename)
    encoded_message = encode_message(book_words, message)
    write_output(output_filename, encoded_message)

if __name__ == "__main__":
    main()
