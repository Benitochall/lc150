class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_str = []

        for char in s:
            if char == '(':
                stack.append(''.join(current_str))
                current_str = []
            elif char == ')':
                current_str.reverse()
                if stack:
                    current_str = list(stack.pop()) + current_str
            else:
                current_str.append(char)

        return ''.join(current_str)

if __name__ == '__main__':
    S = Solution()
    print(S.reverseParentheses('n(ev(t)((()lfevf))yd)cb()'))  # Output: "ndyfvefltvecb"
