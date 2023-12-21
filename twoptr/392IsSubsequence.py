def isSubsequence(s, t):
    i =0
    j =0
    t = list(t)
    if not s:
        return True
    if s and t:
        while j < len(t) and i <len(s):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1
        if (i == len(s)):
            return True
    return False

print(isSubsequence("b","ahbgdc"))