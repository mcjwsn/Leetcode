class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        from heapq import heappop, heappush
        Q = []
        P = []
        n = len(nums[0])
        heappush(Q, "1")
        heappush(Q, "0")
        for _ in range(n-1):
            if not P:
                while Q:
                    a = heappop(Q)
                    heappush(P,a + "1")
                    heappush(P,a + "0")
            else: 
                while P:
                    a = heappop(P)
                    heappush(Q,a + "1")
                    heappush(Q,a + "0")            
        d = {}
        for i in nums: d[i] = 1
        if not P: b = Q
        else: b = P
        while b:
            a = heappop(b)
            if a not in d: return str(a)
        
            