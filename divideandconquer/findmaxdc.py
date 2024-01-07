def findMax(array):
    if len(array) == 1:
        return array[0] 
    else:
        rightMax = findMax(array[:len(array)//2])
        leftMax = findMax(array[(len(array)//2):])

        if rightMax > leftMax:
            return rightMax
        else:
            return leftMax


# print(findMax([1,2,5,7,77,2,3,4,66,44,5,67]))
print(findMax([1,2,5,4,1]))