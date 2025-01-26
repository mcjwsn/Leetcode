class Solution:
    def frequencySort(self, s: str) -> str:
        Up = [0 for _ in range(26)] # 65-90
        Lw = [0 for _ in range(26)] # 97-122
        D = [0 for _ in range(10)] # 48-57
        Total = []
        for i in range(len(s)):
            a = ord(s[i])
            if a<65:
                D[a-48]+=1
                continue
            if a>90:
                Lw[a-97]+=1
                continue
            Up[a-65]+=1
        for i in range(26):
            if Up[i]!=0:
                Total.append([Up[i], chr(i+65)])
            if Lw[i]!=0:
                Total.append([Lw[i], chr(i+97)])
        for i in range(10):
            if D[i]!=0:
                Total.append([D[i], chr(48+i)])
        Total = sorted(Total, key = lambda x: -x[0])
        s = ""
        for i in range(len(Total)):
            for _ in range(Total[i][0]):
                s+=Total[i][1]
        return s