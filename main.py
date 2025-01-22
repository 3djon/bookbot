def count_words(text):
    words = text.split() # adds all individual words into a list
    return len(words) # counts the words in the list

def count_characters(text):
    string_count = {} # dictionary to store counted letters
    text = text.lower() # converts all text to lowercase

    for character in text:
        if character.isalpha(): # only count of its a letter
            if character in string_count:
                string_count[character] += 1 # add one to its count
            else:
                string_count[character] = 1 # start the count at 1
    return string_count

def sort_report(text):
    # Retrieve word counds from function
    word_count = count_words(text)
    # Retrieve character counts from function
    char_counts = count_characters(text)

    # Convert dict to a LIST of dictionaries
    char_list = []
    for char, count in char_counts.items():
        # Create a new dictionary for this character
        char_dict = {'char': char, 'count': count}
        # Add it to our list
        char_list.append(char_dict)
 
    # Defining the helper function
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)

    # Creating the organized report
    print("--- Begin report of books/common_sense.txt ---")
    print(f"{word_count} words found in the document\n")
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    print("--- End report ---")


def main():
    with open("books/common_sense.txt") as f:
        file_contents = f.read() # Reading the contents of text document
        sort_report(file_contents) # Generates a report of amount of words and unique character count of provided text
        
if __name__ == "__main__":
    main()