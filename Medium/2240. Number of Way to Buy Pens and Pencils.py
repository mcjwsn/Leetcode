class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1>total:return total//cost2+1
        if cost2>total:return total//cost1+1
        cnt = 0
        for i in range(total//cost1+1):
            cnt+=(total-i*cost1)//cost2 + 1
        return cnt