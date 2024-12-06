class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        T = [0]*n
        T[-1] = satisfaction[-1]
        for i in range(n-2,-1,-1):
            T[i] = T[i+1] + satisfaction[i]
        cnt = 0
        n-=1
        while n>=0 and T[n]>0:
            cnt+=T[n]
            n-=1
        return cnt