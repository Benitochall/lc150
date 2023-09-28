def jumpGame(nums):

    #idea start at the end of the array 
    if len(nums) == 1:
        return True
    for i in range(0, len(nums)-1):
        # if the index behind can get to the next
        # if the element = 0 we need to go into a for loop 
        amountHoles = nums[i]
        if amountHoles == 0 and i ==0:
            return False
        for j in range(0,nums[i]):
            if amountHoles > 0 and i+j+1 >= len(nums)-1:
                return True
            if nums[i+j+1] == 0:
                amountHoles-=1
            if nums[i+j+1] == 0 and amountHoles ==0:
                return False
    return False
print(jumpGame([1,0,1,0]))