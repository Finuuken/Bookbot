def get_book_text(path):
    with open(path) as f:
        contents = f.read()
        return contents


from stats import count_words, letter_count, sort_on, sort_dict


def main():
	book = get_book_text("books/frankenstein.txt")
	num_words = count_words(book)
	characters = letter_count(book)
	sorted_list = sort_dict(characters)
	
			
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print ("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char_info in sorted_list:
		if char_info["char"].isalpha() == False:
			continue
		else:
			print(f"{char_info["char"]}: {char_info["num"]}")
	print("============= END ===============")
main()

