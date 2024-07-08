class Solution():
    def findOccurances(self, text, pattern):
        if len(pattern) > len(text):
            return 0
        
        base = 31
        modulus = 7
        
        plen = len(pattern)
        tlen = len(text)
        
        phash = 0
        thash = 0
        instances = 0
        
        # Calculate the hash for the pattern and the initial window of text
        for i in range(plen):
            phash = (phash * base + ord(pattern[i])) % modulus
            thash = (thash * base + ord(text[i])) % modulus
        
        # Slide over the text and compare hashes
        for j in range(plen, tlen):
            if phash == thash:
                if text[j-plen:j] == pattern:
                    instances += 1
            
            # Update the hash for the next window in the text
            thash = ((thash - ord(text[j-plen]) * pow(base, plen-1, modulus)) * base + ord(text[j])) % modulus
        
        # Check the last window after the loop
        if phash == thash:
            if text[tlen-plen:tlen] == pattern:
                instances += 1
        
        return instances


if __name__ == '__main__':
    s = Solution()
    s.findOccurances("AABAACAADAABAABA", "AABA")