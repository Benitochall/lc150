#kadanes algo

def findMaxSubarray(array):
    # for each index, the max subbarray at each index is either the current element
    # or the current element with the global max

    global_max = local_max = (array[0], (0,0))

    # at every index starting at 1 we find the max between the current element and the locally
    # computed array up to that element
    # we choose one or the other, then compare to global max
    for i in range(1, len(array)):
        val, pos = local_max
        if array[i] > val + array[i]:
            local_max = (array[i], (i,i))
        else:
            local_max = (val+array[i], (pos[0], i))
        if local_max[0] > global_max[0]:
            global_max = local_max

    return global_max


    

print(findMaxSubarray([1,-3,2,1,-1]))