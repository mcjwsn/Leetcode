from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        s = dict()
        for day in responses:
            d = Counter(day)
            for v in d.keys():
                if v not in s: s[v] = 1
                else: s[v] += 1
        T = []
        for v in s.keys(): T.append((v,s[v]))
        T = sorted(T,key = lambda x: (-x[1],x[0]))
        return T[0][0]