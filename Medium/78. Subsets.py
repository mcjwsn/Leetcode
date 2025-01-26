class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        x = []
        for i in range(len(nums)+1):
            x += list(combinations(nums,i))
        return x