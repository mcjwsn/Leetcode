class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def dSum(n: int) -> int :
            cnt = 0
            while n > 0:
                cnt+=n%10
                n//=10
            return cnt
        nums = sorted(nums, key = lambda x : (dSum(x),x))
        print(nums)
        m = -2
        for i in range(len(nums)-1,0,-1):
            if dSum(nums[i]) == dSum(nums[i-1]):
                m = max(nums[i] + nums[i-1],m)
        return max(m,-1)