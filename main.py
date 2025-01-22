from datetime import datetime
from tabulate import tabulate

def count_words(text):
    words = text.split() # adds all individual words into a list
    return len(words) # counts the words in the list

def count_specific_words(text):
    text = text.lower()
    words = text.split()
    words_to_find = ["america", "government", "liberty", "britain", "tyranny"]
    word_counts = {"america": 0, "government": 0, "liberty": 0, "britain": 0, "tyranny": 0}

    for word in words:
        if word in words_to_find:
            word_counts[word] += 1

    return word_counts


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
    # Retrieve word counts from function
    word_count = count_words(text)
    # Rertieve unique word count from function
    specific_word_count = count_specific_words(text)
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

    def create_table():
        # Calc total characters
        total_chars = sum(char_dict['count'] for char_dict in char_list)

        # Rows with percentages
        rows = []
        for char_dict in char_list:
            char = char_dict['char']
            count = char_dict['count']
            percentage = (count / total_chars) * 100
            rows.append([char, count, f"{percentage:.2f}%"])

        headers = ['Character', 'Occurrences', 'Percentage']
        return tabulate(rows, headers=headers, tablefmt='grid')

    # Creating the organized report
    print("--- Begin report of books/common_sense.txt ---")
    print("")
    print(f"{word_count} words found in the document\n")
    print("\nUnique Word Counts:")
    print("-" * 30)
    for word, count in sorted(specific_word_count.items()):
        print(f"{word:<12} : {count:>5}")
    print("-" * 30)
    print("")
    print("\nCharacter Counts:")
    print(create_table())
    print("\nStats")
    print("-" * 30)
    print(f"Most common character: '{char_list[0]['char']}' ({char_list[0]['count']} times)")
    print(f"Least common character: '{char_list[-1]['char']}' ({char_list[-1]['count']} times)")
    print("")
    print("--- End report ---")
    print(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  


def main():
    with open("books/common_sense.txt") as f:
        file_contents = f.read() # Reading the contents of text document
        sort_report(file_contents) # Generates a report of amount of words and unique character count of provided text
        
if __name__ == "__main__":
    main()