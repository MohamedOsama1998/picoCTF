buffer = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
flagChars = [None] * 32
flag = ""
i = 0

while(i < 8):
	flagChars[i] = buffer[i]
	i += 1

while(i < 16):
	flagChars[23-i] = buffer[i]
	i += 1

while(i < 32):
	flagChars[46-i] = buffer[i]
	i += 2

i = 31

while(i >= 17):
	flagChars[i] = buffer[i]
	i -= 2

for CHAR in flagChars:
	flag += CHAR

print("picoCTF{" + flag + "}")

