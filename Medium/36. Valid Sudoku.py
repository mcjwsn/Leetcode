class Solution(object):
    def isValidSudoku(self, board):
        T = []
        for i in range(1,10): T.append([i,1])
        def lines(B,G):
            T = G
            for j in range(9):
                for i in range(9):
                    if B[j][i]!=".":
                        T[int(B[j][i])-1][1]-=1
                for i in range(9):
                    if T[i][1]<0: return False
                for i in range(9): T[i][1]=1
            return True
        def kol(B,G):
            T = G
            for j in range(9):
                for i in range(9):
                    if B[i][j]!=".":
                        T[int(B[i][j])-1][1]-=1
                for i in range(9):
                    if T[i][1]<0: return False
                for i in range(9): T[i][1]=1
            return True
        S = [] # strats of sqaures
        for i in range(3):
            for j in range(3):
                S.append([3*i,3*j])
        def squares(A,S,T):
            for v in S:
                for i in range(3):
                    for j in range(3):
                        if A[v[0]+i][v[1]+j]!=".":
                            T[int(A[v[0]+i][v[1]+j])-1][1]-=1
                for i in range(9):
                    if T[i][1]<0: return False
                for i in range(9): T[i][1]=1
            return True
        return kol(board,T)*lines(board,T)*squares(board,S,T)
                