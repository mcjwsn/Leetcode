class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        s = {}
        cnt = 0
        for i in range(n):
            if nums[i]-i not in s: s[nums[i]-i] = 1
            else: s[nums[i]-i]+=1
        for i in range(n):
            if nums[i]-i in s:
                cnt+=s[nums[i]-i]-1
        return n*(n-1)//2 - cnt//2