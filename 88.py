def merge(nums1, m, nums2, n):
        # find largest and set as last, contiune until i or j hits 0 
        # then if j still has elements in it but those in
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # this is just merge sort
        # find the min of the two arrays 

        # this solution sorts backwards
        i, j, k = m-1, n-1, m+n-1
        
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        print(nums1)
merge([4,0,0,0,0,0], 1, [1,2,3,5,6], 5)


