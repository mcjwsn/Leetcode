class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for v in nums:
            if v not in d:d[v] =1
            else: d[v] += 1
        cnt = 0
        x = list(d.keys())
        for v in nums:
            if d[v] > 0:
                if k-v == v:
                    if d[v] > 1:
                        d[v] -= 2
                        cnt += 1
                elif k-v > 0 and k-v in d and d[k-v] > 0:
                    cnt += 1
                    d[v] -= 1
                    d[k-v] -= 1
        return cnt