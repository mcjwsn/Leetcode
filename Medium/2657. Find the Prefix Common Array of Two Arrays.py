class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d1 = set()
        d2 = set()
        n = len(A)
        S = []
        cnt = 0
        for i in range(n):
            d1.add(A[i])
            d2.add(B[i])
            if B[i] == A[i]: 
                cnt+=1
                S.append(cnt)
                continue
            if B[i] in d1: cnt+=1
            if A[i] in d2: cnt+=1
            S.append(cnt)
        return S