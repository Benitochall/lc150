class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # first go through each element ant check the dead ones vs alive 
        # then go through and change

        # moore neiborhood
        rows = len(board)
        cols = len(board[0])

        dirs = [(1,1), (-1,-1), (1,0), (0,1), (1,-1), (-1,1), (0,-1), (-1,0)]

        for i in range(rows):
            for j in range(cols):
                # check if cell is alive or dead 
                num_neibors = 0
                for di, dj in dirs:
                    di = di +i 
                    dj = dj + j
                    if 0 <= di < rows and 0 <= dj < cols:
                        if board[di][dj]== 0 or board[di][dj]== 1:
                            num_neibors+= board[di][dj]
                        elif board[di][dj] == 'D':
                            num_neibors+= 1

                    
                if board[i][j] == 1:
                    if num_neibors < 2:
                        board[i][j] = 'D'
                    elif num_neibors > 3:
                        board[i][j] = 'D'
                elif board[i][j] == 0:
                    if num_neibors == 3:
                        board[i][j] = 'A'

        


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'A':
                    board[i][j] = 1
                elif board[i][j] == 'D':
                    board[i][j] = 0



if __name__ == '__main__':
    S = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    S.gameOfLife(board)
