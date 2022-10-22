#!/usr/bin/env python3

import sys


OFFSET = ord('a')
ALPHABET_COUNT = 26


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


# Decrypt the cipher by shifting characters by a value [KEY]
def decrypt(cipher, key):
	dec = ""
	for char in cipher:
		shifted = int(ord(char)) + key
		new_char = chr(shifted % ALPHABET_COUNT + OFFSET)
		dec += new_char

	return dec


# Read ciphertext -> try keys from 0 to 26
def main():
	ciphertext = readFile(sys.argv[1])
	for possible_key in range(ALPHABET_COUNT):
		print(f'Trying key: {possible_key}')
		decoded = decrypt(ciphertext, possible_key)
		print(decoded)


# Kick off
if __name__ == "__main__":
	main()
else:
	print("Please run this script directly\n")
	exit(1)
