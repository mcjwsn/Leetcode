class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        Poss = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,0],[1,-1],[1,1]]
        x,y = king
        cnt = []
        for a,b in Poss:
            kx,ky = x,y
            while -1 < kx < 8 and -1 < ky < 8:
                if [kx,ky] in queens: 
                    cnt.append([kx,ky])
                    break
                kx += a
                ky += b
        return cnt
        