class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[0]+nums[-1]
        n = len(nums)
        for i in range(n//2):
            m = max(m, nums[i]+nums[n-1-i])
        return m