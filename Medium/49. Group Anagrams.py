class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            word = strs[i]
            word = sorted(word,key = lambda x: ord(x))
            word = "".join(word)
            if word in d: d[word].append(strs[i])
            else: d[word] = [strs[i]]
        return list(d.values())
             