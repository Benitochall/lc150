class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        opening_count = 0
        closing_count = 0
        swaps = 0
        for i, letter in enumerate(s):
            if letter == '[':
                opening_count +=1
            elif letter == ']':
                closing_count +=1
            if closing_count > opening_count:
                swaps+=1
                closing_count -=1
                opening_count +=1
        return swaps
# openings should all be on the left side so if closing is greater than opening we need to swap them






        