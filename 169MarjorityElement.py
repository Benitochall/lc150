import math
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list_of_tuples = []
        for num in nums:
            if num in list_of_tuples:
                continue
            else:
                list_of_tuples.append(num)
                if nums.count(num) > math.floor(len(nums)/2):
                    return num

array = [1,2,3,4,4,4,6,6,2,2,3,4,2,2,2,2,2,2,2]
print(majorityElement(array))