def jumpGame(nums):

    # #idea start at the end of the array 
    # if len(nums) == 1:
    #     return True
    # for i in range(0, len(nums)-1):
    #     # if the index behind can get to the next
    #     # if the element = 0 we need to go into a for loop 
    #     amountHoles = nums[i]
    #     if amountHoles == 0 and i ==0:
    #         return False
    #     for j in range(0,nums[i]):
    #         if amountHoles > 0 and i+j+1 >= len(nums)-1:
    #             return True
    #         if nums[i+j+1] == 0:
    #             amountHoles-=1
    #         if nums[i+j+1] == 0 and amountHoles ==0:
    #             return False
    # start at index 0 
    i= 0
    last_index = 0
    prev_last_index = 0 
    for i in range(len(nums)):
        last_index = i
        for j in range(nums[i]):
            last_index+=1
        if nums[i] == 0 and last_index > i:
            if prev_last_index > last_index:
                continue
            else:    
                prev_last_index = last_index
            continue
        elif last_index >= len(nums) -1:
            return True
        elif nums[i] == 0 and prev_last_index <= i:
            return False
        if last_index < prev_last_index:
            continue
        else:
            prev_last_index = last_index
print(jumpGame([5,9,3,2,1,0,2,3,3,1,0,0]))