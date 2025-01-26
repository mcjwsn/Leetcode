class Solution(object):
    def partitionString(self, s):
        d = {}
        n = len(s)
        cnt = 1
        i = 0
        while i < n:
            if s[i] in d:
                cnt+=1
                d = {}
                d[s[i]]=1
            else: d[s[i]]=1
            i+=1
        return cnt
        