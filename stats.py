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
       
    return characters

def sort_on(num):
    return num["num"]

def sort_dict(num):
    number = []
    for ch,count in num.items():
        n = {"char": ch, "num": count}
        number.append(n)
    number.sort(reverse=True, key=sort_on)
    return number


