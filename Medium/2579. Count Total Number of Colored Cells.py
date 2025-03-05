class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * sum(i for i in range(2*n-1,0,-2)) - 2*n + 1