passwordArr = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304867, 942695730, 942748212]

for char in passwordArr:
	char = str(bin(char)[2:10])
	print(chr(int(char)))