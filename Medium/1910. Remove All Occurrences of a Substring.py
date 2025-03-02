class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        i = 0
        n = len(s)
        while i < n:
            #print(s)
            if s[i:i+len(part)] == part:
                s = s[:i] + s[i+len(part):]
                i = max(i-len(part),0)
            else: i+=1
        return s
        
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(s)
        k = len(part)
        i = 0
        while i < n:
            print(s)
            if s[i:i+k] == part:
                s = s[:i] + s[i+k:]
                n-=k
                i-=k
            else: i+=1
        return s