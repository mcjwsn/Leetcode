class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        Sqmax  = int(c**0.5)
        for i in range(Sqmax+1):
            a = (c - i*i)**0.5
            if int(a) == a: return True
        return False