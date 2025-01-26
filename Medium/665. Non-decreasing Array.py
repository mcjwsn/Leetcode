class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def isdc(x):
            for i in range(1,len(x)):
                if x[i] < x[i-1]: return False
            return True
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return isdc(nums[:i-1] + nums[i:]) or isdc(nums[:i] + nums[i+1:])
        return True