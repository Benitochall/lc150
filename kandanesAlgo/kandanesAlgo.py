# kandanes algo is used to find the max subarray of a given set of numbers in o(n) time
def maxSubarraySumCircular(array):
        
    def kanadanesAlgo(array):
        maxSubVal = float('-inf')
        maxSubArrayGlobal = float('-inf')
        current_indicy_array=[]
        for i in range(len(array)):
            currSub = array[i%len(array)]
            if currSub > currSub + maxSubVal:
                maxSubVal = currSub
                current_indicy_array.clear()
                current_indicy_array.append(i%len(array))
            else:
                maxSubVal = currSub + maxSubVal
                current_indicy_array.append(i%len(array))
            if maxSubArrayGlobal < maxSubVal:
                maxSubArrayGlobal = maxSubVal

        return maxSubArrayGlobal
    maxSubArray = kanadanesAlgo(array)
    minSubArray = kanadanesAlgo([-1*x for x in array])

    return maxSubArray maxSubArray - minSubArray
        
