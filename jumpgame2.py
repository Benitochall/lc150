def jumpGame2(nums):

    #idea start at the end of the array 
    jumcntr = 0
    jumpsToTake =0
    i =0
    while i< len(nums)-1:
        i = i+ jumpsToTake


        if i > len(nums)-1:
            continue

        arrJumps= {}
        for j in range(0,nums[i]):
            if j+i+1 >= len(nums):
                continue
            arrJumps.update({j+1 : nums[j+i+1]})

        if arrJumps:
            maxJump = max(arrJumps.items(), key=lambda x: x[1])
        else:
            maxJump = (1,0)

        jumcntr += 1

        # now I need to go to that counter
        i = maxJump[0]+i
        jumpsToTake = maxJump[1]
    return jumcntr




   
print(jumpGame2([2,3,1,1,4]))