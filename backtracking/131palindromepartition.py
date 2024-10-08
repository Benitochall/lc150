def partition(string):
    res = []
    curr = []

    def isPali(i,j):
        if string[i] != string[j]:
            return False
        else:
            i+=1
            j-=1
        return True

    def dfs(i): # i is the current index character 

        # how this algo works
        # we know we havea plidrome because we have checked 
        if i >= len(string):
            res.append(curr[:]) # we append our solution 
            return
        # recursive case
        # need to check if it is a palindrome
        for j in range(i,len(string)):
            # for each letter in from current letter i to j 
            # we check if that sub string is a palendrome
            # if it is we can append it to our list of palindromes
            # it does the longest palindrome at a current index 
            # then continues 
            if isPali(i,j):
                curr.append(string[i:j+1])
                dfs(j+1)
                curr.pop()
    dfs(0)

partition("aab")