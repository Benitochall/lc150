def specialArray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0,len(nums)):
            a = len([x for x in nums if x >= len(nums)-i])
            if a and a == len(nums)-i:
                return a
        return -1
if __name__ == '__main__':
    print(specialArray([3,5]))
    print(specialArray([0,0]))
    print(specialArray([0,4,3,0,4]))
    print(specialArray([3,6,7,7,0]))