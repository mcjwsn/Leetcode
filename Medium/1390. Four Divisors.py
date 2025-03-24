class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divs(n):
            i = 2
            cnt = 2
            s = n+1
            while i*i <= n:
                if n%i == 0:
                    if i*i==n:
                        cnt +=1 
                        i +=1
                        continue
                    cnt +=2 
                    if cnt > 4: break
                    s += i + n//i
                i += 1
            return (cnt == 4,s)
        d = {}
        for v in nums:
            if v not in d:
                d[v] = divs(v)
        return sum(d[v][1] for v in nums if d[v][0] == True)