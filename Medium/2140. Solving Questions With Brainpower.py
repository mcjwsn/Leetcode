class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)
        i = n-1
        while i >= 0:
            dp[i] = max(dp[i+1],questions[i][0]) if i + questions[i][1] + 1 >= n else max(dp[i+questions[i][1]+1] + questions[i][0],dp[i+1])
            i -= 1
        return dp[0]