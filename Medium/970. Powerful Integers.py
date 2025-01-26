class Solution:
    def powerfulIntegers(self, x: int, y: int, bounds: int) -> List[int]:
        xcnt = 0
        ycnt = 0
        b = bounds
        if x>1: 
            while b > 0:
                xcnt+=1
                b//=x
        else: xcnt = 1
        b = bounds
        if y >1:
            while b >0:
                ycnt += 1
                b //= y
        else: ycnt = 1
        xcnt-=1
        ycnt-=1
        s= set()
        for i in range(xcnt+1):
            for j in range(ycnt+1):
                a = x**i + y**j
                if a<= bounds:
                    s.add(a)
                else: break
        return list(s)