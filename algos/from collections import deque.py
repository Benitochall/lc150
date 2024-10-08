from collections import deque

def max_submatrix_sums(matrix):
    m = len(matrix)
    if m == 0:
        return []

    # Step 1: Compute the prefix sum matrix
    prefix_sum = [[0] * (m + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

    # Step 2: Calculate the maximum sum for each n x n submatrix using sliding window
    max_sums = []
    for n in range(1, m + 1):
        max_sum = float('-inf')
        for i in range(n, m + 1):
            row_sums = [0] * (m + 1)
            for j in range(1, m + 1):
                row_sums[j] = prefix_sum[i][j] - prefix_sum[i-n][j]

            # Use deque to find the maximum sum in the sliding window
            deq = deque()
            for j in range(1, m + 1):
                while deq and deq[0] < j - n + 1:
                    deq.popleft()

                while deq and row_sums[deq[-1]] <= row_sums[j]:
                    deq.pop()

                deq.append(j)

                if j >= n:
                    total = row_sums[deq[0]] - (prefix_sum[i][j-n] - prefix_sum[i-n][j-n])
                    max_sum = max(max_sum, total)

        max_sums.append(max_sum)

    return max_sums

# Example usage:
matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

print(max_submatrix_sums(matrix))  # Expected output: [1, 4, 9]