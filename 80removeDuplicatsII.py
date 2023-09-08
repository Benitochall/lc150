def removeDuplicates(nums): 
    unique_ele = []
    count =0 
    for ele in nums:
        if unique_ele.count(ele) < 2:
            count+=1
            unique_ele.append(ele)
    for i, ele in enumerate(unique_ele, start=0):
        nums[i] = ele
    return(len(unique_ele))
        

removeDuplicates([1,1,1,2,2,3])