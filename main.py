import sys
from stats import count_words, letter_count, sort_on, sort_dict

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def main():
    book_path = sys.argv[1]
    book = get_book_text(book_path)
    num_words = count_words(book)
    characters = letter_count(book)
    sorted_list = sort_dict(characters)

    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    for char_info in sorted_list:
        if not char_info["char"].isalpha():
            continue
        else:
            print(f"{char_info['char']}: {char_info['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()


