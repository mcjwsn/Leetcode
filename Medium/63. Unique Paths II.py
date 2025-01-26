class Solution(object):
    def uniquePathsWithObstacles(self, T):
        m = len(T)
        n = len(T[0])
        if T[0][0]==1: return 0
        T[0][0]=1
        for i in range(m):
            for j in range(n):
                if T[i][j]==1 and (i>0 or j>0):
                    T[i][j] = 0
                    continue
                if j-1>=0:
                    T[i][j] += T[i][j-1]
                if i-1>=0:
                    T[i][j]+=T[i-1][j]
        return T[m-1][n-1]
        