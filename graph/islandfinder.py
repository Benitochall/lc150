def numIslands( grid):
  i = 0
  j = 0 
  m = len(grid)
  n = len(grid[0])
  num_islands = 0
  def islander(i,j):
    if i >= 0 and i< m and j >=0 and j < n and grid[i][j] == "1":
        # set this as a zero 
        grid[i][j] = "0"
        # expolore the rest of the grid 
        islander(i+1,j)
        islander(i,j+1)
        islander(i-1,j)
        islander(i,j-1)

  for i in range(m):
      for j in range(n):
              if grid[i][j] =="1":
                  num_islands+=1
                  islander(i,j)
  return num_islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))