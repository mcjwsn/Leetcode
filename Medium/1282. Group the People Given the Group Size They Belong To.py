class Solution(object):
    def groupThePeople(self, groupSizes):
        n = len(groupSizes)
        G = []
        S = [[] for _ in range(n+1)]
        for i in range(n):
            S[groupSizes[i]].append(i)
            if len(S[groupSizes[i]]) == groupSizes[i]:
                G.append(S[groupSizes[i]])
                S[groupSizes[i]] = []
        return G
        