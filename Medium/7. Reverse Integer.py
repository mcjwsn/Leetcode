class Solution(object):
    def reverse(self, x):
        if x> 2147483646 or x<-2147483647: return 0
        val = 1
        x = str(x)
        if len(x)==10 and int(x[9])> 2: return 0    
        if int(x)<0:
            val = -1
            x=x[1:]
        sum = 0
        y = len(x)
        while y>1:
            sum+=int(x[y-1])*(10**(y-1))
            y-=1
        sum += int(x[0])
        if sum> 2147483646: return 0
        return sum*val