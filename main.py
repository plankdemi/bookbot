from stats import get_number_of_words, get_char_repetition, sorted_list
from sys import argv
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents



def main():


    if(len(argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(argv[1])
    num_of_words = get_number_of_words(text)


    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")


    char_array = sorted_list(get_char_repetition(text))

    
    print("--------- Character Count -------")

    for element in char_array:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")

    print("============= END ===============")
    #print(sorted_list(get_char_repetition(text)))


main()