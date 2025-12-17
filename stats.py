def count_words(text):
	
	count = len(text.split())
	return count

def letter_count(text):
    characters = {}
    lower = text.lower()

    for char in lower:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
        characters.sort(reverse=True, key=sort_on)
    return characters

