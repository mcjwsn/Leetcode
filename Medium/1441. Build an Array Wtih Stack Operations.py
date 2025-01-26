class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        start = 1
        i = 1
        T = []
        while i <n+1:
            T.append("Push")
            if target[-1] == i: break
            if i not in target:
                T.append("Pop")
            i+=1
        return T
        