# the key to this algo is to run a binary search 
# Take element in the middle of the list, if greater than explore right, if less than explore right 
def binarySearch(nums, target):
    if not nums:
        return False

    # get the middle number 
    mid = nums[len(nums)//2]
    if mid == target:
        return True
    elif mid > target:
        if binarySearch(nums[:len(nums)//2], target):
            return True
        else:
            return False
    else:
        if binarySearch(nums[len(nums)//2+1:], target):
            return True
        else:
            return False
        
def binarySearchIterative(nums, target):
    i = 0
    j = len(nums) - 1

    while i < j:
        m = (i + j) //2
        mid = nums[m]
        if mid == target:
            return True
        elif mid > target:
            j = (i + j) //2 -1
        else:
            i = (i + j) //2 +1
    return False
    
    

print(binarySearchIterative([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100], 100))
