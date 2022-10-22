#!/usr/bin/env python3


import sys, string


CHARS = string.ascii_uppercase
ALPHABET_COUNT = 26
OFFSET = ord("A")


# Validate input
if len(sys.argv) != 3:
	print("Usage: decrypt.py [ciphertext filename] [key filename]\nExiting...\n")
	exit(1)


# Read ciphertext from a file
def readCipher(cname):
	try:
		with open(cname, "r") as ifile:
			ciphertext = ifile.readline().strip()
	except:
		print(f'Error occured while trying to read the file {cname}\nExiting...\n')
		exit(1)
	return ciphertext


# Read key from a file
def readKey(kname):
	try:
		with open(kname, "r") as ifile:
			key = ifile.readline().strip()
	except:
		print(f'Error occured while trying to read the file {kname}\nExiting...\n')
		exit(1)
	return key


# Decode ciphertext using the provided key
def decode(cipher, key):
	dec = ""
	for i, c in enumerate(cipher):
		shift = CHARS.index(key[i])
		new_c = ((ord(c) - OFFSET - shift) % ALPHABET_COUNT)
		dec += chr(new_c + OFFSET)

	return dec


# Read ciphertext and key from files, decode cipher and print it
def main():
	ciphertext = readCipher(sys.argv[1])
	key = readKey(sys.argv[2])
	plain = decode(ciphertext, key)
	print(plain)


# Kick off
if __name__ == "__main__":
	main()
else:
	print("Please run this script directly\nExiting...\n")
	exit(1)
