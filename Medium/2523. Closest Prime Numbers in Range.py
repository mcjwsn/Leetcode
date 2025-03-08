class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def isPrime(x: int) -> bool:
            if x < 2 : return False
            if x%2==0 or x%3==0: return False
            i = 5
            while i*i <= x:
                if x%i==0: return False
                i += 1
            return True
        d = {}
        if left<2 and right>3:
            return [2,3]
        for i in range(left,right+1):
            if isPrime(i):
                d[i] = 1
                if i-2 in d: return [i-2,i]
        primes = list(d.keys())
        if len(primes) < 2: return [-1,-1]
        m = right - left + 1
        val = None
       # print(primes)
        for i in range(1,len(primes)):
            if primes[i]-primes[i-1] < m:
                m = primes[i]-primes[i-1]
                val = i
        return [primes[val-1],primes[val]]