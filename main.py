from stats import get_num_words, get_char_count
import sys

def get_book_text(file_path):
    file = open(file_path, "r")
    return file.read()

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = sys.argv[1]
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f"Found {get_num_words(get_book_text(file_path))} total words")
    print('--------- Character Count -------')
    char_count = get_char_count(get_book_text(file_path))
    for char in char_count:
        print(f'{char}: {char_count[char]}')
    print('============= END ===============')

main()