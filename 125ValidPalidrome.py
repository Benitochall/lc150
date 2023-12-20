
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    isPal = ""
    s = s.lower()
    for letter in s:
        if letter.isalpha():
            newLetter = letter.lower()
            isPal += newLetter
    strLen = len(isPal)
    print(isPal)

    if strLen %2 == 0:
        for i in range(0, strLen/2):
            if isPal[i] == isPal[strLen-1-i]:
                continue
            else:
                return False
    else:
        for i in range(0, strLen//2):
            if isPal[i] == isPal[strLen-1-i]:
                continue
            else:
                return False
    return True




print(isPalindrome("A man, a plan, a canal: Panama"))