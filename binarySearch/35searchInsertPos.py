# the key to this algo is to run a binary search 
# Take element in the middle of the list, if greater than explore right, if less than explore right 
def binarySearch(nums, target, start):
    if len(nums) == 0: # this is if nothing is found we return the start index
        return start
    middle = len(nums) // 2
    find = nums[middle]

    if find == target:
        return start + middle
    elif target > find:
        return binarySearch(nums[middle + 1:], target, start + middle + 1)
    else:
        return binarySearch(nums[:middle], target, start)

print(binarySearch([1,3,5,6],5,0))
