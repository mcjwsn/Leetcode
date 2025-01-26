class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        Checked = [[False for _ in range(len(board[0]))]for _ in range(len(board))]
        cnt = 0
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and Checked[i][j] == False:
                    Checked[i][j] = True
                    cnt+=1
                    for k in range(i+1,n):
                        if board[k][j] == 'X': Checked[k][j] = True
                        else: break
                    for k in range(j+1,m):
                        if board[i][k] == 'X': Checked[i][k] = True
                        else: break
        return cnt