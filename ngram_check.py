#!/usr/bin/env python3

import argparse

def main(file_path, ignore_list, length, top, includeany_list, includeall_list):
	debug_limit = 0

	# Initialize a dictionary to store n-gram frequencies
	ngram_frequency = {}

	# Open the text file in read mode
	with open(file_path, 'r') as file:
		# Read the contents of the file
		text = file.read()

		count = 0
		# Iterate through the text in groups of characters
		for i in range(len(text) - (length - 1)):
			ngram = text[i:i+length].lower()
			count += 1
			if debug_limit and count == debug_limit:
				break
			# Check if the ngram contains any ignored characters
			if (  
				all(char.isalpha() for char in ngram) and
				not any(char in ignore_list for char in ngram) and
				(len(includeany_list) == 0 or any(char in includeany_list for char in ngram)) and
				(len(includeall_list) == 0 or all(req_char in ngram for req_char in includeall_list))
			):
				# Update the frequency in the dictionary
				if ngram in ngram_frequency:
					ngram_frequency[ngram] += 1
				else:
					ngram_frequency[ngram] = 1

	# Print the ngram frequencies, sorted from most to least frequent
	n = 1
	for ngram, frequency in reversed(sorted(ngram_frequency.items(), key=lambda item: item[1])):
		if top and n > top:
			break
		print(f"{n} - {ngram}: {frequency}")
		n += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate n-gram frequencies in a text file.")
    parser.add_argument("file_path", help="Path to the text file")
    parser.add_argument("--ignore", nargs='*', default=[], help="List of characters to ignore")
    parser.add_argument("--length", default=2, help="Length of n-grams to calculate. Default is 2.")
    parser.add_argument("--top", default=20, help="Only show top N results. default is 50.")
    parser.add_argument("--includeany", nargs='*', default=[], help="List of characters the n-gram has to include (any of them)")
    parser.add_argument("--includeall", nargs='*', default=[], help="List of characters the n-gram has to include (all of them)")
    args = parser.parse_args()
    main(args.file_path, args.ignore, int(args.length), int(args.top), args.includeany, args.includeall)