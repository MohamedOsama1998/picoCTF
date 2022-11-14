decimalChars = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98]
hexChars = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
octChars = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o70 , 0o146]
asciiChars = ['4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b']
flag = ""

for CHAR in decimalChars:
	flag += chr(CHAR)

for CHAR in hexChars:
	flag += chr(CHAR)

for CHAR in octChars:
	flag += chr(CHAR)

for CHAR in asciiChars:
	flag += CHAR

print("picoCTF{" + flag + "}")
