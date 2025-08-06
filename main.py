from stats import *
import sys

def get_book_text(path:str) -> str:
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main(path:str):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book = get_book_text(path=path)

    print(f"----------- Word Count ----------")
    print(f"Found {word_count(book)} total words")

    char_count_dict = char_count(book)
    sorted_chars = sorted_char_count(char_count_dict)
    print("--------- Character Count -------")
    for count in sorted_chars:
        print(f"{count['char']}: {count['num']}")
    print("============= END ===============")
    

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        main(sys.argv[1])


