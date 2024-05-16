def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    if len(nums) < 3:
            return []
            
    return_nums = []
    sorted_arr = sorted(nums)

    for i in range(len(sorted_arr)-2):
        # need to take care of duplicate i's because we have already added them
        if nums[i] > 0 or nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(sorted_arr) -1
        # close them in on each other 
        while l <r:
            s = sorted_arr[i] + sorted_arr[l] + sorted_arr[r]
            if s <0:
                l+=1
            elif s > 0:
                r-=1
            else:
                found_zero = [sorted_arr[i], sorted_arr[l],  sorted_arr[r]]
                return_nums.append([sorted_arr[i], sorted_arr[l],  sorted_arr[r]])
                # it is possible we have not moved on to differnt numbers yet
                while l<r and sorted_arr[l] == found_zero[1]:
                    l+=1
                while r>l and sorted_arr[r] == found_zero[2]:
                    r-=1
            
    return return_nums

print(threeSum([0,0,0]))