class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = sorted(words,key = lambda x: -len(x))
        m = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[i]) * len(words[j]) <= m: break
                A = set()
                B = set()
                for v in words[i]:A.add(v)
                for v in words[j]:B.add(v)
                if len(A & B) == 0: m = max(m,len(words[i]) * len(words[j]))
        return m