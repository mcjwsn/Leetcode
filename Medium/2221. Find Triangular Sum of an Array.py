class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        from math import comb
        n = len(nums)
        x = [comb(n-1,k) for k in range(n//2)]
        mid = []
        if n%2==1: mid.append(comb(n-1,n//2))
        x = x + mid + x[::-1]
        s = 0
        for i in range(n): s += (x[i]*nums[i]) 
        return s % 10