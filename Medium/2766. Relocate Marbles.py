class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        d = dict()
        # d[pozycja] = kulki
        for i in range(len(nums)):
            d[nums[i]] = [i]
        for i in range(len(moveFrom)):
            v = moveFrom[i]
            a = d[v]
            d[v] = []
            w = moveTo[i]
            if w in d:
                for x in a:d[w].append(x)
            else: d[w] = a
        res = []
        for v in d:
            if len(d[v])>0:
                res.append(v)
        return sorted(res)