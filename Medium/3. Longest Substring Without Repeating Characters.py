class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        d = {}
        n = len(s)
        start = 0
        m = 0
        occ = 0
        for i in range(n):
            if s[i] not in d: d[s[i]] = i
            else:
                if not occ:
                    m = i 
                    occ = 1
                m = max(m,i-start -1)
                start = max(d[s[i]],start)
                d[s[i]] = i
        if not occ: return len(s)
        return max(m,n-start-1)