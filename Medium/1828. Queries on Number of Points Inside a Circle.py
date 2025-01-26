class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        q = len(queries)
        T = [0 for _ in range(q)]
        for i in range(q):
            v = queries[i]
            for p in points:
                if v[2] >= ((v[1]-p[1])**2 + (v[0]-p[0])**2)**0.5:
                    T[i]+=1
        return T