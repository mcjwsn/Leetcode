class Solution(object):
    def jump(self, nums):
        n = len(nums)
        jumps = [-1]*n
        jumps[0] = 0
        for i in range(n):
            for j in range(1,nums[i]+1):
                if j+i<n:
                    if jumps[i+j]==-1 or jumps[i+j]>jumps[i]+1:
                        jumps[i+j] = jumps[i]+1
                else: break
        return jumps[-1]