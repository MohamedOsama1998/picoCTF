password = [None] * 32
passwordString = ""

password[0]  = 'd'
password[29] = '9' 
password[4] = 'r' 
password[2] = '5' 
password[23] = 'r' 
password[3] = 'c' 
password[17] = '4' 
password[1] = '3' 
password[7] = 'b' 
password[10] = '_' 
password[5] = '4' 
password[9] = '3' 
password[11] = 't' 
password[15] = 'c' 
password[8] = 'l' 
password[12] = 'H' 
password[20] = 'c' 
password[14] = '_' 
password[6] = 'm' 
password[24] = '5' 
password[18] = 'r' 
password[13] = '3' 
password[19] = '4' 
password[21] = 'T' 
password[16] = 'H' 
password[27] = '5' 
password[30] = '2' 
password[25] = '_' 
password[22] = '3' 
password[28] = '0' 
password[26] = '7' 
password[31] = 'e'

for letter in password:
    passwordString += letter

print("picoCTF{" + passwordString + "}")