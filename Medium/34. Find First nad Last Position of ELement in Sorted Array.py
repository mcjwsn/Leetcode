class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first = nums.index(target)
            a = first
        else: return [-1,-1]
        while first < len(nums) and nums[first] == target:first+=1
        return [a,first-1]