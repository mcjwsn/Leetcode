class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        mx = 0
        n = len(s)
        i = 1
        if n==1: return 1
        while i < n:
            cnt = 1
            while i < n and ord(s[i-1]) == ord(s[i])-1:
                cnt+=1
                i+=1
            mx = max(mx,cnt)
            i+=1
        return mx
            
            