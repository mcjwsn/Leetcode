class Solution(object):
    def appendCharacters(self, s, t):
        cnt = 0
        a = len(s)
        b = len(t)
        for i in range(a):
            if s[i] == t[cnt]:
                cnt+=1
            if cnt == b: return 0
        return b-cnt
        