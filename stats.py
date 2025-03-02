def word_count(text):
	return len(text.split())

def char_count(text, filter=False):
	results = {}
	for c in text.lower():
		if not filter or (filter and filter(c)):
			results[c] = results.get(c, 0)+1

	return results
