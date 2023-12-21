def spiralOrder(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    sizeofMatrix = rows * cols
    visited = []
    tuples = set()
    i, j = 0, 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(sizeofMatrix):
        visited.append(matrix[i][j])
        tuples.add((i, j))

        ni, nj = i + directions[0][0], j + directions[0][1]

        if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in tuples:
            i, j = ni, nj
        else:
            directions.append(directions.pop(0)) # oh it resuffles the direction of change
            i, j = i + directions[0][0], j + directions[0][1]

    return visited



print(spiralOrder([[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]))
       