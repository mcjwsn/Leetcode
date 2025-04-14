class Solution(object):
    def tupleSameProduct(self, nums):
        d = {}
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                a = nums[i] * nums[j]
                if a not in d: d[a] = 1
                else: d[a] += 1
        return sum((a-1)*a//2 for a in d.values())*8
        