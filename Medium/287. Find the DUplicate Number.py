class Solution(object):
    def findDuplicate(self, nums):
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]: return nums[i]
        