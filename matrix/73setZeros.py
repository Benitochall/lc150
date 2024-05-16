def setZeroes(matrix):

    touched = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0 and (i,j) not in touched:
                # set all row I to 0
                for k in range(0,len(matrix)):
                    if matrix[k][j] == 0:
                        continue 
                    elif (k,j) not in touched:
                        matrix[k][j] = 0
                        touched.append((k,j))
                    
                for h in range(0,len(matrix[0])):
                    if matrix[i][h] == 0:
                        continue 
                    elif (i,h) not in touched:
                        matrix[i][h] = 0
                        touched.append((i,h))

print(setZeroes([[0,1]]))