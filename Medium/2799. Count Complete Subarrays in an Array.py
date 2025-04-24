class Solution(object):
    def countCompleteSubarrays(self, nums):
        from collections import Counter
        s = Counter(nums)
        for v in s: s[v] = 0
        need = len(s.keys())
        cnt = 0
        res = 0
        start = 0
        end = len(nums)
        curr = 0
        while curr < end:
            if cnt < need:
                if s[nums[curr]] == 0: cnt += 1
                s[nums[curr]] += 1
                curr += 1
            else:
                res += end - curr + 1
                if s[nums[start]] == 1: cnt -= 1
                s[nums[start]] -= 1
                start += 1
        while need == cnt:
            res += 1
            if s[nums[start]] == 1: cnt -= 1
            s[nums[start]] -= 1
            start += 1
        return res 