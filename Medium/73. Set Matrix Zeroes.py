class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)
        for v in rows:
            for j in range(m):
                matrix[v][j] = 0
        for v in columns:
            for i in range(n):
                matrix[i][v] = 0