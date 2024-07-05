def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                intersection.append(nums1[i])

intersect([2,2],[1,2,2,1])