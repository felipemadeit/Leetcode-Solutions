def numberOfSpecialChars(self, word: str):
    """Returns the number of special chars in a given string

    Args:
        word (str): String to evaluate 
    """
    # Time Complexity : O(n)
    
    non_repeat = list(set(word))
    print(non_repeat)
    special_chars = 0
    
    for i in non_repeat:
        if i.lower() in non_repeat and i.upper() in non_repeat:
            special_chars += 1
    print(special_chars // 2)
    
    

        


numberOfSpecialChars(numberOfSpecialChars, 'abBCab')
    