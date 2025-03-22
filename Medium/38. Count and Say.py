class Solution:
    def countAndSay(self, n: int) -> str:
        x = "1"
        for _ in range(n-1):
            print(x)
            y = len(x)
            k = ""
            i = 0
            while i < y:
                cnt = 1
                j = 1
                while i + j < y and x[i] == x[i+j]:
                    cnt += 1
                    j += 1
                k += str(cnt) + x[i]
                i+=j
            x = k
        return x