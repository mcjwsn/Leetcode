class Solution(object):
    def maxBottlesDrunk(self, nb, ne):
        s = empty = 0
        while empty+nb>=ne:
            s+=nb
            empty+= nb
            cnt = 0
            while empty >= ne:
                empty-=ne
                ne+=1
                cnt+=1
            nb = cnt
        return s + nb   
        