def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # I think I can use slices for this
    if len(nums) == 2 and k > len(nums):
        nums[:] = nums[::-1]
    else:
        nums[:] = nums[len(nums)-k:len(nums)] + nums[:len(nums)-k]
    return nums

print(rotate([1,2,3,4,5], 3))

