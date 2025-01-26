class Solution:
    def getSum(self, a: int, b: int) -> int:
        T = []
        if a>=0:
            if b>=0:
                for _ in range(a):
                    T.append(None)  
                for _ in range(b):
                    T.append(None)
                return len(T)
            else:
                for i in range(max(a,abs(b))):
                    T.append(None)
                for i in range(min(a,abs(b))):
                    T.pop()
                if a > abs(b): 
                    return len(T)
                else: return -len(T)
        else:
            if b<0:
                for _ in range((abs(a))):
                    T.append(None)  
                for _ in range(abs(b)):
                    T.append(None)
                return -len(T)
            else:
                for i in range(max(b,abs(a))):
                    T.append(None)
                for i in range(min(b,abs(a))):
                    T.pop()
                if abs(a) < b: 
                    return len(T)
                else: return -len(T)