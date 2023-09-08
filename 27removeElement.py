def removeElement(nums, val):
    num_val = nums.count(val)
    while (num_val != 0):
        nums.remove(val)
        num_val = nums.count(val)



    print(nums)
removeElement([3,2,2,3], 3)