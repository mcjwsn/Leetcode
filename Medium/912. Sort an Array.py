class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        from heapq import heappop, heappush
        T = []
        Q = []
        heappush(Q, nums[0])
        for i in range(1,len(nums)):
            heappush(Q, nums[i])
        for i in range(len(nums)):
            T.append(heappop(Q))
        return T