def isPalindrome(self, x: int):
    """Return if the num is palindrome

    Args:
        x (int): num to evaluate
    """
    if str(x)[::-1] == str(x):
        print("true")
    else:
        print("false")

isPalindrome(isPalindrome, 121)
    