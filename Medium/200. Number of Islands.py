class Solution(object):
    def numIslands(self, grid):
        n = len(grid)
        m = len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        C = []
        T = [(1,0),(-1,0),(0,-1),(0,1),(0,0)]
        def BFS(i,j,val):
            for a,b in T:
                if 0 <= i+a < len(grid) and 0 <= j+b < len(grid[0]) and visited[i+a][j+b] == False and grid[i+a][j+b] == '1':
                    visited[i+a][j+b] = True
                    BFS(i+a,j+b,val)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == '1':
                    C.append(0)
                    BFS(i,j,len(C)-1)

        return len(C)