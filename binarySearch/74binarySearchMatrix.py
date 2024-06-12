
def searchMatrix(matrix, target):
    """
    key flatten the matrix to be a 1D array and do binary search 
    so after each iteration, we move the left and right to be the mid + 1 or mid - 1 effictivly cutting the array in half
    the key to flattening the matrix is find the half way point of the 1d arrary
    then we can find the row and col of the 2d array by mid // cols and mid % cols --- important
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
        
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t= 3
print(searchMatrix(m,t))
