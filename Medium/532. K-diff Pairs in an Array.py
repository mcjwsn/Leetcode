class Solution(object):
    def findPairs(self, nums, k):
        if k==0:
            d = dict()
            for v in nums:
                if v not in d: d[v] = 1
                else: d[v]+=1
            s = 0
            for v in d:
                if d[v] >1:
                    s += 1
            return s
        s = 0
        d = dict()
        for v in nums:
            d[v] = 1
        for v in d.keys():
            if v+k in d:
                s += 1
        return s
        