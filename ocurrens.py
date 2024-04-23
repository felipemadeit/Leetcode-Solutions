def count_substring(string, sub_string):
    
    ocurrens = 0

    for letters in range(0, len(string)-1):
        if string[letters] == 'C' and string[letters+1] == 'D' and string[letters+2] == 'C':
            ocurrens += 1
    return ocurrens
 

print(count_substring("ABCDCDC", "CDC"))