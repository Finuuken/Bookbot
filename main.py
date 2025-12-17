def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents


from stats import count_words, letter_count


def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = count_words(book)
    characters = letter_count(book)

    print(f"Found {num_words} total words")
    print(characters)


main()

