class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = {}
        for v in arr:
            if v not in d: d[v] = 1
            else: d[v] += 1
        arr.sort()
        m = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                start = arr[i]
                mid = arr[j]
                cnt = 0
                end = arr[j] + arr[i]
                if end in d:
                    while end in d:
                        cnt += 1
                        start = mid
                        mid = end
                        end += start
                    m = max(m,cnt+2)
        return m