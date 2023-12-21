import re
def isValidSudoku(board):

    pattern = re.compile(r'^[1-9]$')

    if len(board) != 9:
        return False
    cols = [[],[],[],[],[],[],[],[],[]]
    boxes = [[],[],[]]
    for i in range(0,9):
        if len(array[i]) != 9:
            # this is the case where the array is not of len 9
            return False
        # now is where I build my arrays
        if i%3 == 0:
            boxes = [[],[],[]] # reset the boxes 
        currRow = []
        for j in range(0,9):
            # check if the element is in the list
            # need to check if the element is between 1 and 9 and is an integer and not in 
            currVal = board[i][j]
            if currVal == '.': #handle case where element is blank
                continue
            val = pattern.match(currVal)
            if not val or (currVal in currRow) or (currVal in cols[j]) or (currVal in boxes[j//3]):
                return False
            else:
                # need to add to three things 
                # 1 the currRow
                currRow.append(currVal)
                # 2 the current col
                cols[j].append(currVal)
                #3 the correct box 
                boxes[j//3].append(currVal)

    return True
    
array = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(array))