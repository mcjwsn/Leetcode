class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        Acnt = 0
        Bcnt = 0
        x = ""
        while a + b > 0:
            if a == 0: return x + b*"b"
            if b == 0: return x + a*"a"
            if Acnt == 2:
                x += "b"
                Acnt = 0
                b-=1
                Bcnt = 1
                continue
            if Bcnt == 2:
                x += "a"
                Acnt = 1
                a -= 1
                Bcnt = 0
                continue
            if a > b:
                x += "a"
                a-=1
                Acnt+=1
                Bcnt = 0
                continue
            if b >= a:
                x += "b"
                b -=1
                Bcnt+=1
                Acnt = 0
        return x