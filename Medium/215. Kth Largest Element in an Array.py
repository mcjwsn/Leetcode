class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush, heappop
        Q = [ ]
        for i in range(k):
            heappush(Q,nums[i])
        for i in range(k,len(nums)):
            x = nums[i]
            y = heappop(Q)
            heappush(Q,max(x,y))
        return heappop(Q)