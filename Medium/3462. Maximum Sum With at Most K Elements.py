class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        T = []
        if k ==0: return 0
        from heapq import heappush, heappop
        for i in range(len(grid)):
            row = grid[i]
            limit = limits[i]
            if limit == 0: continue
            Q = []
            for j in range(min(limit, len(row))):
                heappush(Q,row[j])
            #print(Q)
            for j in range(min(limit, len(row)),len(row)):
                a = heappop(Q)
                heappush(Q,max(a,row[j]))
                #print(Q)
            T += Q
        T.sort()
        #print(T)
        return sum(T[len(T)-k:])