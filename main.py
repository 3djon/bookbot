def count_words(text):
    words = text.split() # adds all individual words into a list
    return len(words) # counts the words in the list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # reading the contents of above file
        word_count = count_words(file_contents) # calling word count function
        print(f"Word count: {word_count}") # This displays the full book text to terminal

if __name__ == "__main__":
    main()