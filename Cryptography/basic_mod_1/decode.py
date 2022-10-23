#!/usr/bin/env python3


import sys, string


# Validate input
if len(sys.argv) != 2:
	print("Usage: decrypt.py [ciphertext filename] [key filename]\nExiting...\n")
	exit(1)


# Read ciphertext from a file
def readCipher(cname):
	ciphertext = []
	try:
		with open(cname, "r") as ifile:
			lines = ifile.readline().strip()
			ciphertext = lines.split(" ")
	except:
		print(f'Error occured while trying to read the file {cname}\nExiting...\n')
		exit(1)
	return ciphertext


def createMap():
	char_set = ""
	# Letters
	char_set = string.ascii_uppercase
	# Numbers
	for i in range(10):
		char_set += str(i)
	# Underscore
	char_set += "_"

	return char_set


# Decode ciphertext 
def decode(cipher, char_set):
	dec = ""
	for char in cipher:
		i = int(char) % 37
		dec += char_set[i]

	return dec


# Read ciphertext and key from files, decode cipher and print it
def main():
	ciphertext = readCipher(sys.argv[1])
	char_set = createMap()
	decoded = decode(ciphertext, char_set)
	print("picoCTF{" + decoded + "}")


# Kick off
if __name__ == "__main__":
	main()
else:
	print("Please run this script directly\nExiting...\n")
	exit(1)
