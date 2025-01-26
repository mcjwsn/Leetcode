class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        i = 1
        while i < n:
            if s[i]=="*":
                s = s[:i-1] + s[i+1:]
                n-=2
                i-=1
            else: i+=1
        return s