import sys
from stats import get_num_words, get_num_chars, get_sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_txt(book):
    with open(book) as book_opened:
        book_string = book_opened.read()
    return book_string

def main():
    book_in_string = get_book_txt(sys.argv[1])
    number_of_words = get_num_words(book_in_string)
    num_chars = get_num_chars(book_in_string)
    sorted_list = get_sorted_list(num_chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for dicts in sorted_list:
        if dicts["char"].isalpha():
            print(f"{dicts["char"]}: {dicts["num"]}")
    print("============= END ===============")

main()