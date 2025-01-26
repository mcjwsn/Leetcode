class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heappush, heappop
        Q = []
        cnt = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if cnt > k:
                    c = -heappop(Q)
                    if c > matrix[i][j]:
                        heappush(Q,-matrix[i][j])
                    else: heappush(Q,-c)
                else: 
                    heappush(Q,-matrix[i][j])
                    cnt+=1
        #print(Q)
        return -heappop(Q)