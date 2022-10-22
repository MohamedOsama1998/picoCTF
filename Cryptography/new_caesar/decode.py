#!/usr/bin/env python3

import sys, string


# Global Variables
LOWERCASE_OFFSET = ord("a")
LOWER_CASE_CHARS = string.ascii_lowercase[:16]


# Validate input
if len(sys.argv) != 2:
	print("Usage: decrypt.py [FILENAME]\nExiting...\n")
	exit(1)


# Read ciphertext from a file
def readFile(fname):
	try:
		with open(fname, "r") as ifile:
			ciphertext = ifile.readline().strip()
	except:
		print("Error occured while trying to read the file\nExiting...\n")
		exit(1)
	return ciphertext


# Decode from b16 to a string - Reversing the picoCTF algorithm
def b16_decode(text):
	plain = ""
	for i in range(0, len(text), 2):
		first_four_bits = "{0:04b}".format(LOWER_CASE_CHARS.index(text[i]))
		second_four_bits = "{0:04b}".format(LOWER_CASE_CHARS.index(text[i + 1]))
		char_in_ascii = first_four_bits + second_four_bits
		char = chr(int(char_in_ascii, 2))
		plain += char
	
	return plain


# Reverse the shifting function
def unshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return LOWER_CASE_CHARS[(t1 - t2) % len(LOWER_CASE_CHARS)]


# Decoding the ciphertext
def decode(cipher, key):
	dec = ""
	for i, c in enumerate(cipher):
		dec += unshift(c, key[i % len(key)])
	
	return dec


# Read ciphertext -> decode it using all key possibilities
# Keys can only be one character long, and in the first half of the alphabet
def main():
	ciphertext = readFile(sys.argv[1])
	for possible_key in LOWER_CASE_CHARS:
		print(f'Now trying key: {possible_key}')
		b16 = decode(ciphertext, possible_key)
		plain = b16_decode(b16)
		print(plain)


# Kick off
if __name__ == "__main__":
	main()
else:
	print("Please run this script directly..\n")
	exit(1)

# Key is "G"
# Flag: picoCTF{et_tu?_5723f4e71a0736d3b1d19dde4279ac03}
