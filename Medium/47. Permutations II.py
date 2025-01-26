class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        x = list(permutations(nums))
        a = dict()
        for v in x:
            if v not in a:
                a[v] = 1
        return list(a.keys())