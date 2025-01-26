class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        T = [i for i in range(1,n+1)]
        return list(combinations(T,k))