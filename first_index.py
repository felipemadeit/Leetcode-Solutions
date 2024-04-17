first_string = input()
second_string = input()

if second_string in first_string:
    print(first_string.index(second_string))
else:
    print("-1")