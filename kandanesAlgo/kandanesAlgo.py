# kandanes algo is used to find the max subarray of a given set of numbers in o(n) time
def kandane(array):
    maxSubVal = float('-inf')
    maxSubArrayGlobal = float('-inf')
    for i in range(len(array)):
        currSub = array[i]
        if currSub > currSub + maxSubVal:
            maxSubVal = currSub
        else:
            maxSubVal = currSub+ maxSubVal
        if maxSubArrayGlobal < maxSubVal:
            maxSubArrayGlobal = maxSubVal

    return maxSubArrayGlobal
        
print(kandane([5,4,-1,7,8]))