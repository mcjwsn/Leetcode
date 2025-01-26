class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = [False ]*n
        from heapq import heappop, heappush
        Q = []
        for i in range(n):
            heappush(Q,(nums[i],i))
        score = 0
        for i in range(n):
            val, idx = heappop(Q)
            if marked[idx] == True: continue
            score += val
            marked[idx] = True
            if idx+1<n: marked[idx+1] = True
            if idx-1>-1:marked[idx-1] = True
        return score