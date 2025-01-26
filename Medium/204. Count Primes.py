class Solution:
    def countPrimes(self, n: int) -> int:
        d = {}
        cnt = 0
        for i in range(2,n):d[i] = True
        i = 2
        while i*i<n:
            if d[i]==True:
                cnt+=1
                j = 2
                while j*i < n:
                    d[j*i] = False
                    j+=1
            i+=1
        return sum(d.values())