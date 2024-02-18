def removeDuplicates(nums):
    uniqueNums = []
    count =0
    
    for item in nums:
        if item not in uniqueNums:
            count +=1
            uniqueNums.append(item)
    nums = []
    nums = uniqueNums
    return count

removeDuplicates([1,1,2,2,3,3,3])