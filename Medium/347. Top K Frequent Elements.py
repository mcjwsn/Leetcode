class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for v in nums:
            if v not in s: s[v] = 1
            else: s[v] +=1
        n = list(s.keys())
        #print(n)
        Q = []
        from heapq import heappush, heappop
        for i in range(k):
            heappush(Q,(s[n[i]],n[i]))
        for i in range(k,len(n)):
            a,b = heappop(Q)
            if s[n[i]] > a: heappush(Q,(s[n[i]],n[i]))
            else:heappush(Q,(a,b))
        return [x[1] for x in Q]