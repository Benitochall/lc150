from collections import deque
# note most graph traversal algos use queues, and a while quue loop with a q.pop
def solve(board):
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])
    queue = deque()

    def mark_border_connected(r, c):
        if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
            queue.append((r, c))
            board[r][c] = 'B'

    for i in range(rows):
        mark_border_connected(i, 0)
        mark_border_connected(i, cols - 1)
    for j in range(cols):
        mark_border_connected(0, j)
        mark_border_connected(rows - 1, j)

    # TODO: study this for a graph traversing interview
    
    while queue:
        r, c = queue.popleft() # pull the latest value off of the queue
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                board[nr][nc] = 'B'
                queue.append((nr, nc))

    # Step 2: Flip all remaining 'O's to 'X', and turn back 'B' to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'B':
                board[r][c] = 'O'

# Example usage
board = [["O","X","X","O","X"],
         ["X","O","O","X","O"],
         ["X","O","X","O","X"],
         ["O","X","O","O","O"],
         ["X","X","O","X","O"]]
solve(board)
for row in board:
    print(row)
