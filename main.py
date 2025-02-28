#!/usr/bin/python3

def word_count(text):
	return len(text.split())

def char_count(text, filter=False):
	results = {}
	for c in text.lower():
		if not filter or (filter and filter(c)):
			results[c] = results.get(c, 0)+1

	return results

def book_text(target):
	with open(target) as f:
		return f.read()

def test(x):
	print(x[1])
	return 1

def book_report(book_path):
	book = book_text(book_path)
	words = word_count(book)
	chars = sorted(list(char_count(book, lambda c: c.isalpha()).items()), key=lambda x: -x[1])


	print (f'''--- Begin report of {book_path[2:]} ---

    {words} total words found in the document.
''')

	for char in chars:
		print (f"    The '{char[0]}' character was found {char[1]} times")

	print("\n--- End report ---\n--- May I go outside and play now? ---")

def main():

	book_report("./books/frankenstein.txt")

main()
