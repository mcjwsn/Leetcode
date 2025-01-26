class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        T = [0 for _ in range(len(edges))]
        for i in range(len(edges)):
            T[edges[i]]+=i
        return T.index(max(T))