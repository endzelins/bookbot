#-- imports --
from stats import get_word_count
from stats import get_char_count
from stats import create_list
import sys

#-- static variables --
#path_to_file = "./books/frankenstein.txt"

if len(sys.argv) < 2:
    print(sys.argv, " Usage: python3 main.py <path_to_book>")
    sys.exit(1)
elif len(sys.argv) > 2:
    print(sys.argv, " Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_file = sys.argv[1]

#-- main --
def main():
    word_count, book_str = get_word_count(path_to_file)
    print(f"Found {word_count} total words")
    char_dict = get_char_count(book_str)
    total_list = create_list(char_dict)
    for dict in total_list:
        if dict["char"].isalpha():
            text = (f"{dict["char"]}: {dict["num"]}")
            print(text)
        else:
            continue

#-- execution --
main()
