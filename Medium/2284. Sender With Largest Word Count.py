class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        d = {}
        n = len(senders)
        for i in range(n):
            if senders[i] not in d:
                d[senders[i]] = len(messages[i].split(' '))
            else: d[senders[i]] += len(messages[i].split(' '))
        m = max(d.values())
        T = []
        for v in d:
            if d[v] == m: T.append(v)
        T.sort()
        return T[-1]