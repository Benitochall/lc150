def kSmallestPairs(nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        u_len = len(nums1)
        v_len = len(nums2)
        _max = max(u_len, v_len)
        nums1.extend([-1]* (_max-u_len))
        nums2.extend([-1]* (_max-v_len))

        min_list = []
        i=0
        j=0

        while len(min_list) < k:
            # find the min element
            if nums1[i] < nums2[j]:
                if nums1[i+1] + nums2[j] < nums1[i] + nums2[j]:
                    i+=1
                    j-=1
                min_list.append([nums1[i], nums2[j]])
                j+=1
            else:
                min_list.append([nums1[i], nums2[j]])
                i+=1

        return min_list

print(kSmallestPairs([1,2,4,5,6],[3,5,7,9],3))