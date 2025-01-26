class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        nmbr = n
        cnt = 0
        while nmbr>1:
            nmbr/=3
            cnt+=1
        cnt-=1
        T = []
        T.append(False)
        def rek(i,b):
            if i==1 and b == False: 
                T[0]=True
                return 0
            if i%3==0: rek(i/3, False)
            if b== False: rek(i-1, True)
            return 0
        rek(n,False)
        return T[0]