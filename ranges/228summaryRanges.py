def summaryRanges(nums):
    #need to iterate through the list 
    ranges = []
    i = 0
    if nums:
        j = nums[0]
        while i < len(nums):
            range = j
            endRange = j
            while i < len(nums)-1 and endRange+ 1 == nums[i+1]:
                endRange = nums[i+1]
                i+=1
            i+=1
            if range == endRange:
                ranges.append(f"{range}")
            else:
                ranges.append(f"{range}->{endRange}")
            if i < len(nums):
                j = nums[i]
    return(ranges)

print(summaryRanges([0,1,2,4,5,7]))