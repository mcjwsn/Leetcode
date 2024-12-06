class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        end = n
        if s == s[::-1]: return s
        while s[:end] != s[:end][::-1]:
            end-=1
        return s[end:][::-1] + s