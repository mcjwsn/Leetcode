class Solution:
    def shiftingLetters(self, s: str, T: List[int]) -> str:
        w=""
        n = len(s)
        T[-1]%=26
        def shift(x,num): #97-122
            if ord(x)+num>122: num-=26
            return chr(ord(x)+num)
        for i in range(len(T)-2,-1,-1):
            T[i]+=T[i+1]
            T[i]%=26
        for i in range(n):
            w+=shift(s[i],T[i])
        return w