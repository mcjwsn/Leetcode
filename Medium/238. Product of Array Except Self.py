class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCnt = 0
        for v in nums:
            if v == 0: zeroCnt += 1
            else: prod *= v
        if zeroCnt > 1:
            return [0] * len(nums)
        if zeroCnt == 1:
            x = nums.index(0)
            return [0]*x + [prod] + [0]*(len(nums)-1-x)
        #print(nums)
        return [prod//v for v in nums]