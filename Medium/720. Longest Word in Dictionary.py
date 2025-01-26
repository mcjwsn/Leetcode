class Solution:
    def longestWord(self, words: List[str]) -> str:
        a = set()
        for v in words: a.add(v)
        T = sorted(words, key = lambda x: (-len(x),x))
        for word in T:
            n = len(word) 
            while n>0 and word[:n] in a:n-=1
            if n==0: return word
        return ""