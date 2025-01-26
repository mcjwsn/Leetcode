class Solution:
    def occurrencesOfElement(self, nums: List[int], q: List[int], x: int) -> List[int]:
        d = []
        n = len(nums)
        for i in range(n):
            if nums[i] == x:
                d.append(i)
        p = len(d)
        for i in range(len(q)):
            if q[i] > p:
                q[i]=-1
            else: q[i] = d[q[i]-1]
        return q