class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 1
        if len(points) == 2: return 2
        def calculateLine(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            if x1 == x2: return x1,None
            a = (y1-y2)/(x1-x2)
            b = y1 - x1*a
            return (a,b)
        n = len(points)
        d = {}
        for i in range(n):
            for j in range(i+1,n):
                (a,b) = calculateLine(points[i],points[j])
                if (a,b) in d:
                    d[(a,b)].add((points[i][0],points[i][1]))
                    d[(a,b)].add((points[j][0],points[j][1]))
                else:
                    d[(a,b)] = set()
                    d[(a,b)].add((points[i][0],points[i][1]))
                    d[(a,b)].add((points[j][0],points[j][1]))
        x = list(d.values())
        x.append([0])
        return len(max(x, key = lambda y: len(y)))