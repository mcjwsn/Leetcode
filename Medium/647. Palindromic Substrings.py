class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for start in range(n):
            for end in range(start,n):
                a = s[start:end+1]
                if a == a[::-1]:cnt+=1
        return cnt
                