class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        n = len(s)
        unique_values = list(set(list(s)))
        print(unique_values)
        for i in unique_values:
            l = 0
            h = 0
            replaced =0 

            while h < n:
                if i == s[h]:
                    # we can move h
                    h+=1
                elif replaced < k:
                    h+=1
                    replaced +=1
                elif i == s[l]:
                    l+=1
                else:
                    replaced -=1
                    l+=1
                ans = max(ans, h-l)
        return ans