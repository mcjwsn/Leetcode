class Solution(object):
    def findTheCity(self, n, G, distanceThreshold):
        from heapq import heappush, heappop
        N = [[]for _ in range(n)]
        for v in G:
            N[v[0]].append([v[1],v[2]])
            N[v[1]].append([v[0],v[2]])
    # Dijkstra
        def Dijkstra(G,start):
            n=len(G)
            d=[float("inf") for _ in range(n)]
            d[start]=0
            Q = []
            heappush(Q,(0,start))
            while Q:
                w,u=heappop(Q)
                if w==d[u]:
                    for v,c in G[u]:
                        if relax(d,v,c,u):
                            heappush(Q,(d[v],v))
            return d
        def relax(d,v,c,u):
            if d[v]>d[u]+c:
                d[v]=d[u]+c
                return True
            return False
        m = float("inf")
        m_id = 0
        for i in range(n):
            x = Dijkstra(N,i)
            cnt = 0
            for j in range(len(x)):
                if i!=j and x[j] <=distanceThreshold:
                    cnt+=1
            if cnt<=m:
                m = cnt
                m_id = i
        return m_id 
        