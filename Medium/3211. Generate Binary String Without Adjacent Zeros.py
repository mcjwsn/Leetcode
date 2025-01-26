class Solution:
    def validStrings(self, n: int) -> List[str]:
        from queue import Queue
        from copy import copy
        T = ["0","1"]
        if n == 1: return T
        P = Queue()
        L = Queue()
        P.put(T[0])
        P.put(T[1])
        for _ in range(n-1):
            if L.empty():
                while not P.empty():
                    a = P.get()
                    if a[-1] == "1":
                        b = copy(a)
                        L.put(b+"1")
                        L.put(a+"0")
                    else: L.put(a+"1")
            else: 
                while not L.empty():
                    a = L.get()
                    if a[-1] == "1":
                        b = copy(a)
                        P.put(b+"1")
                        P.put(a+"0")
                    else: P.put(a+"1")
        T = []
        if L.empty():
            while not P.empty():
                T.append(P.get())
        else: 
            while not L.empty():
                T.append(L.get())
        return T