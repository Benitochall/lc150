class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        #4 choose 2, 4 numbers choosing 2
        def backtrack(start, current_combination):
            # If the current combination is of length k, add it to the result
            if len(current_combination) == k:
                combins.append(current_combination[:])
                return
        
            for i in range(start, len(n)):
                current_combination.append(n[i])
                backtrack(i + 1, current_combination)
                current_combination.pop()
        combins = []
        n = list(range(1,n+1))

        backtrack(0,[])
        print(5//2)
        return combins



def main():
    a = Solution()
    c = a.combine(4,2)
if __name__ == '__main__':
    main()