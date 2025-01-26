class Solution:
    def sortVowels(self, s: str) -> str:
        V = ['a', 'e', 'i', 'o','u','A','E','I','O','U']
        W = []
        n = len(s)
        for i in range(n):
            if s[i] in V:
                W.append(s[i])
        W.sort()
        a = ""
        j = 0
        for i in range(n):
            if s[i] in V:
                a+=W[j]
                j+=1
            else:
                a+=s[i]
        return a