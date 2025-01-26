class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        C = defaultdict(int)
        d = {} # pilka i kolor
        n = len(queries)
        cnt = 0
        T = []
        for i in range(n):
            color = queries[i][1]
            ball = queries[i][0]
            if ball not in d:
                d[ball] = color
                if C[color]==0:
                    cnt+=1
                C[color]+=1
            else:
                pcol = d[ball]
                d[ball] = color
                C[pcol]-=1
                if C[pcol]==0: cnt-=1
                if C[color]==0: cnt+=1
                C[color]+=1
            T.append(cnt)
        return T