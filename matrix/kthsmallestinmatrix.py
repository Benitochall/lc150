def kthSmallest(matrix, k):

    def countless(matrix, midval, cols):
        # Count elements less than midval in the matrix
        count = 0
        for i in range(len(matrix)):
            j = 0
            while j < cols and matrix[i][j] <= midval:
                j += 1
            count += j
        return count

    if not matrix or not matrix[0]:
        return None
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = matrix[0][0], matrix[rows - 1][cols - 1]

    while left < right:
        mid = (left + right) // 2
        count = countless(matrix, mid, cols)
        
        if count < k:
            left = mid + 1
        else:
            right = mid

    return left


m = [[1,3,5],[6,7,12],[11,14,14]]
t= 5
print(kthSmallest(m,t))