class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5
        dp = [[0,0,0,0,0] for _ in range(n-1)]
        for i in range(5):
            dp[0][i] = 5-i
        for i in range(1,n-1):
            dp[i][0] = sum(dp[i-1])
            for j in range(1,5):
                dp[i][j] = dp[i][j-1] - dp[i-1][j-1]
        return sum(dp[-1])           