class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 1
        n = len(nums)
        nums = [0] + nums
        while i < n+1:
            if nums[i]<n+1 and nums[nums[i]]!= nums[i]:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
            else:
                i+=1
        T = []
        for i in range(n+1):
            if nums[i]!=i:
                T.append(nums[i])
        return T
                