class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import defaultdict
        a  =list(s)
        b = list(t)
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for ch in a:
            d1[ch]+=1
        for ch in b:
            d2[ch]+=1
        a = d1.keys()
        b = d2.keys()
        cnt = 0
        for ch in a:
            if d1[ch] > d2[ch]:cnt += d1[ch] - d2[ch]
        return cnt