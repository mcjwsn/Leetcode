class Solution(object):
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        V = [[0 for _ in range (m)]for _ in range(n)]
        V[0][0] = grid[0][0]
        for i in range(1,n):
            V[i][0]=V[i-1][0]+grid[i][0]
        for j in range(1,m):
            V[0][j]=V[0][j-1]+grid[0][j]
        for i in range(1,n):
            for j in range(1,m):
                V[i][j] = grid[i][j] + min(V[i-1][j],V[i][j-1])
        return V[-1][-1]