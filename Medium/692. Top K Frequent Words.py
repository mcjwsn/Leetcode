class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = { }
        n = len(words)
        for i in range(n):
            if words[i] not in d:
                d[words[i]] = 1
            else: d[words[i]]+=1
        d = sorted(d.items(),key = lambda item: item[0])
        d = sorted(d, key = lambda x:-x[1])
        T = []
        for i in range(k):
            T.append(d[i][0])
        return T