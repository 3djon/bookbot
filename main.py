def count_words(text):
    words = text.split() # adds all individual words into a list
    return len(words) # counts the words in the list

def count_characters(text):
    string_count = {} # dictionary to store counted letters
    text = text.lower() # converts all text to lowercase

    for character in text:
        if character in string_count:
            string_count[character] += 1 # add one to its count
        else:
            string_count[character] = 1 # start the count at 1
    # Create a sorted version for display
    sorted_chars = dict(sorted(string_count.items()))
    return sorted_chars


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # reading the contents of above file
        word_count = count_words(file_contents) # calling word count function
        char_count = count_characters(file_contents)# calling character counting function
        print(char_count)

if __name__ == "__main__":
    main()