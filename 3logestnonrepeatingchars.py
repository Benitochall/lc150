def lengthOfLongestSubstring(s):
        if not s: 
            return 0
        longestSub = 0
        right, left = 0,0
        uniqueSet = []
        while right < len(s):
            if s[right] not in uniqueSet:
                uniqueSet.append(s[right])
                right+=1
                longestSub = max(longestSub, right-left)
                # i think in this case we want to slide
            elif s[right] in uniqueSet:
                uniqueSet.remove(s[left])
                left+=1
        
        if longestSub == 0:
            longestSub = max(longestSub, right-left)
                 
        return longestSub

print(lengthOfLongestSubstring("pwwkew"))