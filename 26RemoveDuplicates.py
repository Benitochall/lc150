import Math
def removeDuplicates(nums): 
    unique_ele = []
    for ele in nums:
        if ele not in unique_ele:
            unique_ele.append(ele)
    nums = unique_ele

    print(nums, len(nums))

removeDuplicates([1,2,2,3,5,6,66,4,7,9])