class Solution(object):
    def uniquePaths(self, m, n):
        T = [[ 0 for _ in range(n)]for _ in range(m)]
        T[0][0]=1
        for i in range(m):
            for j in range(n):
                if j-1>=0:
                    T[i][j] += T[i][j-1]
                if i-1>=0:
                    T[i][j]+=T[i-1][j]
        return T[m-1][n-1]