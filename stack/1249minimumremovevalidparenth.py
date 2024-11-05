class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        outside = []
        for i, letter in enumerate(s):
            if letter == '(':
                stack.append(i)
            elif letter == ')':
                if stack:
                    stack.pop()
                else:
                    outside.append(i)
        s = list(s)
        for pos in outside:
            s[pos] = 'X'
        for pos in stack:
            s[pos] = 'X'

        re = ''
        for x in s:
            if x != 'X':
                re +=x

        return re
        