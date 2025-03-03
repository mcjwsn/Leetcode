class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        cnt = 0
        L = []
        R = []
        for v in nums:
            if v == pivot:
                cnt+=1
                continue
            if v > pivot: R.append(v)
            else: L.append(v)
        return L + [pivot] * cnt + R
