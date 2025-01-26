class Solution:
    def reverseWords(self, s: str) -> str:
        #n = len(s)
        #i = 1
        #while s[-1] == " " and n>1:
         #   s = s[:n-1]
          #  n-=1
        #while s[0] == " ": s = s[1:]
        #n = len(s)
        #while i<n:
         #   if s[i] == s[i-1] == " ":
          #      s = s[:i-1] + s[i:]
           #     n-=1
            #    continue
            #i+=1
       # T = []
        #start = 0
        #for i in range(n):
         #   if s[i] == " ":
          #      T.append(s[start:i])
           #     start = i+1
        #T.append(s[start:])
        #w= ""
        #for i in range(len(T)-1,0,-1):
         #   w += T[i] + " "
        #w+= T[0]
        #return w
        return " ".join(list(reversed(s.split())))