def longestSubarraywithsumk(array, k):
    # this is an example of a fixed sliding window

    # we are trying to maximize the size of the subarray
    i,j = 0,0
    s = 0
    maxLen = 0
    d = {}
    for i in range(len(array)-1):
        # keepadding until hit k
        s += array[i]

        if s == k:
            maxLen = i+1
        if s not in d: 
            d.update({s:i})
        if s - k in d:
            x = d.get(s-k)
            if maxLen < (i-x):
                maxLen = i-x




   

if __name__ == '__main__':
    longestSubarraywithsumk([10, 5, 2, 7, 1, 9 ], 15)