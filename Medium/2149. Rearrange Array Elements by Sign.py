class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        P = []
        M = []
        for i in range(len(nums)):
            if nums[i]>0: P.append(nums[i])
            else: M.append(nums[i])
        for i in range(len(P)):
            nums[2*i] = P[i]
            nums[2*i+1] = M[i]
        return nums