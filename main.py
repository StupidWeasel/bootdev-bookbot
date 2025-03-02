#!/usr/bin/python3

import sys
from pathlib import Path
from stats import word_count, char_count

def book_text(target):
	with open(target) as f:
		return f.read()

def test(x):
	print(x[1])
	return 1

def book_report(book_path):
	book = book_text(book_path)
	book_name = book_path.name
	words = word_count(book)
	chars = sorted(list(char_count(book, lambda c: c.isalpha()).items()), key=lambda x: -x[1])
	print (f'''--- Begin report of {book_name} ---

    {words} words found in the document.
''')

	for char in chars:
		print (f"    Found {char[0]}: {char[1]} times")

	print("\n--- End report ---\n--- May I go outside and play now? ---")

def main():

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    book_path = Path(sys.argv[1])

    if not (book_path.exists() or book_path.is_file()):
        print("That is not a valid file.")
        sys.exit(1)

    book_report(book_path)

main()
