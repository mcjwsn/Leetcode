class Solution:
    def colorTheArray(self, m: int, queries: List[List[int]]) -> List[int]:
        T = []
        colors = [0 for _ in range(m+1)]
        colors[queries[0][0]] = queries[0][1]
        curr = 0
        T.append(curr)
        n = len(queries)
        for i in range(1,n):
            a = queries[i][0] # index
            b = queries[i][1] # color
            if a-1>=0:
                if colors[a-1] == colors[a] and colors[a]!=0: curr-=1
            if a+1<m+1:
                if colors[a+1] == colors[a]and colors[a]!=0: curr-=1
            colors[a] = b
            if a-1>=0:
                if colors[a-1] == colors[a] and colors[a]!=0: curr+=1
            if a+1<m+1:
                if colors[a+1] == colors[a] and colors[a]!=0: curr+=1
            T.append(curr)
        return T