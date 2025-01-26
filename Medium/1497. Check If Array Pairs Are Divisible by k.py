class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d= {}
        for i in range(k):
            d[i] = 0
        for i in range(len(arr)):
            d[arr[i]%k]+=1
        if d[0]%2==1: return False
        for i in range(1,k//2+1):
            if d[i] != d[k-i]: return False
        return True