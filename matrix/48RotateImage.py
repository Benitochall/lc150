def rotate(matrix):
    #     (0,0)-> (0,n-1), (0,n-1) -> (n-1, n-1), (n-1, n-1) -> (n-1, 0), (n-1, 0) -> (0,0)
    #     (0,1)-> (1,n-1), (1,n-1) -> (n-1, n-2), (n-1, n-2) -> (n-2,0),  (n-2, 0) -> (0,1) 
    #     (0,2)-> (2,n-1), (2, n-1) -> (n-1, 1, 
    amount_rot = len(matrix) // 2 

    for k in range(amount_rot):
        mover = 0 +k# this is our mover columne 
        j=0 +k
        max_i_mov = len(matrix)-1 - 1* k # this is our mover columne 
        max_j = len(matrix)-1 -1* k
        # at each step we need to maintain an I an j
        for _ in range(len(matrix)-1 -2* k):
            matrix[j][mover], matrix[max_i_mov][j], matrix[max_j][max_i_mov], matrix[mover][max_j] = matrix[max_i_mov][j], matrix[max_j][max_i_mov], matrix[mover][max_j], matrix[j][mover]
            mover+=1
            max_i_mov-=1
        k+=1


    



print(rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))
       