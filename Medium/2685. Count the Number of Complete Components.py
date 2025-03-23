class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = [set() for _ in range(n)]
        for i in range(n):
            G[i].add(i)
        for v,w in edges:
            G[v].add(w)
            G[w].add(v)
        cnt = 0
        T = [0 for _ in range(n)]
        for i in range(n):
            S = G[i]
            flag = False
            for v in G[i]:
                if S != G[v]:
                    flag = True
                    break
            if not flag: T[min(G[i])] = 1
        return sum(T)