
def largestNumber( nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    def check_larger_number(l,r):
        #return true if the left number should come before the right number 
        if int(str(l) +str(r)) > int(str(r) +str(l)):
            return True
        else:
            return False

    def breakdown(array):
        # if len
        if len(array) == 1:
            return array
        else:
            middle = len(array)//2
            right = breakdown(array[middle:])
            left = breakdown(array[:middle])
        

        return merge(left,right)

    def merge(left, right):
    # Assume this function correctly merges two sorted arrays
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if check_larger_number(left[i],right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return ''.join([str(x) for x in breakdown(nums)])

print(largestNumber([3,30,34,5,9]))