def spiralOrder(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    sizeofMatrix = rows * cols
    visited = []
    tuples = []
    i=0
    j=0
    hotkey = 'r'
    # maybe have a discoberd matris with a tuple of i,j pairs 
    while len(visited) < sizeofMatrix:
        # add the 0,0 element
        #visited.append(matrix[i][j])
        if hotkey == 'r':
            # check if j < less than hotkey
            if j == cols -1 or ((i,j+1) in tuples):
                # this is the case where we have to turn
                visited.append(matrix[i][j])
                tuples.append((i,j))
                hotkey = 'd'
                i+=1
            else:
                visited.append(matrix[i][j])
                tuples.append((i,j))
                j+=1
        elif hotkey == 'd':
            if i == rows -1 or ((i+1,j) in tuples):
                # this is the case where we have to turn
                visited.append(matrix[i][j])
                tuples.append((i,j))
                hotkey = 'l'
                j-=1
            else:
                visited.append(matrix[i][j])
                tuples.append((i,j))
                i+=1
        elif hotkey == 'l':
            if j == 0 or ((i,j-1) in tuples):
                # this is the case where we have to turn
                visited.append(matrix[i][j])
                tuples.append((i,j))
                hotkey = 'u'
                i-=1
            else:
                visited.append(matrix[i][j])
                tuples.append((i,j))
                j-=1
        else:
            if i == 0 or ((i-1,j) in tuples):
                # this is the case where we have to turn
                visited.append(matrix[i][j])
                tuples.append((i,j))
                hotkey = 'r'
                j+=1
            else:
                visited.append(matrix[i][j])
                tuples.append((i,j))
                i-=1

    return visited


print(spiralOrder([[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]))
       