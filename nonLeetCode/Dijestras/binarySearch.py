def binary_search(array, target):
    if not array:
        return False
    
    left,right = 0, len(array) -1

    while left <= right:
        # find midpoint 
        mid = (left +right) // 2 
        mid_target = array[mid]

        if mid_target == target:
            return True
        elif mid_target > target:
            right = mid -1
        else:
            left = mid +1
    return False

def binary_search_recursive(array, target):

    if not array:
        return False
    
    # calculate the middle of the array
    mid = len(array)//2

    if array[mid] == target:
        return True
    
    elif array[mid] > target:
        # the left half 
        return binary_search_recursive(array[:mid], target)
    else:
        return binary_search_recursive(array[mid+1:], target)



print(binary_search([1,2,3,4,5,6,7,8,9,11,22,34,342,2345,2346], 12))
print(binary_search_recursive([1,2,3,4,5,6,7,8,9,11,22,34,342,2345,2346], 12))