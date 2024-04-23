s = input()

string_final = ''

for letters in s:
    if letters.isdigit():
        string_final += str(bin(letters))
    elif letters.isalpha():
        string_final += str(bin(ord(letters))[2:])
    else:
        string_final += letters

print(string_final)