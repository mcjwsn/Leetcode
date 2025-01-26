class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0: return 0
        if n==1: return nums[0]
        T = [[0,0] for _ in range(n)]
        T[0][1] = T[1][0] = nums[0]
        T[1][1] = nums[1]
        # 0 bez, 1 z
        for i in range(2,n):
            T[i][0] = max(T[i-1][1], T[i-2][0],T[i-2][1])
            T[i][1] = max(T[i-1][0],T[i-2][0],T[i-2][1]) + nums[i]
        return max(T[len(nums)-1])