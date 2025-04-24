class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        from collections import Counter
        def matching(pattern,word):
            if len(list(Counter(pattern).values())) != len(list(Counter(word).values())): return False
            s = {}
            n = len(word)
            m = len(word)
            if n != m : return False
            for i in range(n):
                if word[i] not in s: s[word[i]] = pattern[i]
                elif s[word[i]] != pattern[i]: return False
            return True

        return [word for word in words if matching(pattern,word)]
