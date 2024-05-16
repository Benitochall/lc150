def minimumTotal(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # need to start with the last row of triangle filled in 
        for i in range(len(triangle)-2, -1, -1):
            #iterate backwards through the array 
            for j in range(len(triangle[i])):
                # we want to add the minimum of i+1 and 
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
                print(triangle[i][j])

        return triangle[0][0]

if __name__ == "__main__":
     minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])