
t = input()
first = ''
second = ''

for letters in t:
    if letters.isupper():
        first += letters
    else:
        second += letters

print('\n'.join([first, second]))