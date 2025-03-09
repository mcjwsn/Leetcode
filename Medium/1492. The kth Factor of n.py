class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        L = []
        R = []
        i = 1
        if n ==1 : 
            if k == 1: return 1
            return -1
        while i*i<n:
            if n%i == 0:
                L.append(i)
                R = [n//i] + R
            i += 1
        
        if i<=n and n%i == 0 and L[-1] != i and R[0] != i: L.append(i)
        L += R
        #print(L)
        #print(len(L))
        if len(L) < k: return -1
        return L[k-1]