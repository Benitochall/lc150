def snakesAndLadders(board):
    # idea create a bfs algo to go through every postion 
    # need a way to keep track of the current postion 
    n = len(board)
    def boustrophedon_mapping(n):
        mapping = {}
        count = 1
        for i in range(n - 1, -1, -1): # starting at the last row and going to row 0 in the arrayr
            if (n - i) % 2 == 0:
                for j in range(n - 1, -1, -1): # this is how you iterte backwards through an array
                    mapping[count] = (i, j,board[i][j])
                    count += 1
            else:
                for j in range(n):  # Left to right
                    mapping[count] = (i, j,board[i][j])
                    count += 1

        return mapping
    resulting_mapping = boustrophedon_mapping(n)
    print(resulting_mapping)
    # we are trying to get to position 0,n-1
    visited  = []
    queue = []
    # might be easier to create a dictionary of mappings from numbers to postions 
    # get the first number 
    queue.append((1,0))
    visited.append((1,0))
    not36 =1
    while len(queue) > 0 and not36:
        #queue = sorted(queue, key=lambda x: resulting_mapping[x[0]][2], reverse=True)
        queue = sorted(queue, key=lambda x: x[0], reverse=True)

        num,move = queue.pop(0)
        i,j,k = resulting_mapping[num]
        if board[i][j] == 32:
            pass
        if  board[i][j] != -1:
            # this is the case where we have a later or a snake 
            add = (board[i][j],move)
            if add not in visited:
                queue.append(add)
                visited.append(add)
            if move+1 > n**2:
                not36 = 0
            continue
        # need to add all possible moves to visted and if unvisted put in queue
        for i in range(1,7):
            # push node to visited n-n
            if num + i > n**2:
                break
            add = (num+i,move+1)
            if add not in visited:
                queue.append(add)
                visited.append(add)
            if move+1 > n**2:
                not36 = 0

        # append all the possible blac

    final = [a for a in visited if a[0] == n**2]
    min = 100000
    for num in final:
        if num[1] < min:
            min = num[1]
    if min == 100000:
        return -1
    return min 

board = [[-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,35,-1,-1,13,-1],
         [-1,-1,-1,-1,-1,-1],
         [-1,15,-1,-1,-1,-1]]

board3 = [[-1,-1,30,14,15,-1],
          [23,9,-1,-1,-1,9],
          [12,5,7,24,-1,30],
          [10,-1,-1,-1,25,17],
          [32,-1,28,-1,-1,32],
          [-1,-1,23,-1,13,19]]

board2 = [[-1,-1],[-1,3]]

print(snakesAndLadders(board3))
        