class Solution:
    def minPartitions(self, n: str) -> int:
        '''mx = 0 #48,57
        for i in range(len(n)):
            if ord(n[i]) > mx: mx = ord(n[i])
        return mx-48'''
        return int(max(n))