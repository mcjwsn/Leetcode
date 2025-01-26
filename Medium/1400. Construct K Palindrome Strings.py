class Solution(object):
    def canConstruct(self, s, k):
        d = {}
        a = len(s)
        if a < k: return False
        if a ==k : return True
        for v in s: 
            if v in d: d[v] = (d[v]+1)%2
            else : d[v] = 1
        x = list(d.values())
        return sum(x)<k+1  
        