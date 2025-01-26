class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        d = defaultdict(int)
        for i in matches:
            d[i[1]]+=1
            if i[0] not in d: d[i[0]] = 0
        N = []
        S = []
        for key in d.keys():
            if d[key] == 0: N.append(key)
            if d[key] == 1: S.append(key)
        N.sort()
        S.sort()
        return [N,S]