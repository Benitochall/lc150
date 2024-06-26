class Solution(object):
    def dfs(self, board, i, j, word, count, visited):
        # Base case: if count equals the length of word, we found the word
        if count == len(word):
            return True
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and (ni, nj) not in visited:
                if board[ni][nj] == word[count]:
                    visited.add((ni, nj))
                    if self.dfs(board, ni, nj, word, count + 1, visited):
                        return True
                    visited.remove((ni, nj))  # Backtrack
        
        return False
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Edge case: if word is empty
        if not word:
            return False
        
        # Iterate through the board to find the starting point for the word
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    if self.dfs(board, i, j, word, 1, visited):
                        return True
        
        return False
