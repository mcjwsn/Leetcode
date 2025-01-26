class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1: return int((n-1)/2 * ((n-1)/2+1))
        else: return n//2 + int((n//2 - 1) * n//2)