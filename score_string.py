def score_string (self, s: str):
    """Returns the score of the string 

    Args:
        s (str): String to calculate her score
    """
    
    # Complexity  Big (O) -> O(n)
    
    score = 0
    
    for letters in range(len(s)-1):
        score += abs(ord(s[letters])- ord(s[letters+1]))
    
    print(score)

score_string(score_string,"zaz")