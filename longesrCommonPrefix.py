def longestCommonPrefix(self, strs: list):
    """Return the common prefix, else ""

    Args:
        strs (list): list with worlds
    """
    prefix = ""
    
    for worlds in strs:
        prefix += worlds[:2]
    if prefix == worlds[:2]*len(strs):
        print(f"'{worlds[:2]}'")
    else:
        print("''")
    
    
    
            
longestCommonPrefix(longestCommonPrefix, strs=["dog","racecar","car"])