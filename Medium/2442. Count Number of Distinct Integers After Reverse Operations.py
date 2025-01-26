class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            v = nums[i]
            v = str(v)
            v = v[::-1]
            v = int(v)
            nums.append(v)
        s =dict()
        for v in nums:
            if v not in s:
                s[v] = 1
        return len(list(s.keys()))