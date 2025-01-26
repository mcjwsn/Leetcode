class Solution:
    def firstMissingPositive(self, nums) -> int:
        i = 0
        const_n = len(nums)
        while i < const_n:
            if nums[i]<1 or nums[i]>= const_n:
                i+=1
            else:
                if nums[i] == nums[nums[i]-1]:
                    i+=1
                else: 
                    nums[nums[i]-1],nums[i] = nums[i], nums[nums[i]-1]
        for i in range(const_n):
            if nums[i]!=i+1: return i+1
        return const_n+1