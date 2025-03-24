class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        if n == 1 or n ==2 or n==4 or n ==8:return True
        d = Counter(str(n))
        m = int("9" * len(str(n)))
        i = 1
        while i < m:
            if d == Counter(str(i)): return True
            i *= 2
        return False