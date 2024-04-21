s = input()
new_string = s.split(' ')


final_string = ''

for index, letters in enumerate(new_string):
    if index == 1:
        final_string += letters[0].upper() + letters[1:]
    else:
        final_string +=letters

print(final_string)
    


