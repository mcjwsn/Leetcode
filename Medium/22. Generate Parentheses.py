class Solution(object):
    def generateParenthesis(self, n):
        T = []
        string = ""
        def rek(left,right,string,T):
            if left == right == 0:
                T.append(string)
            if left == right and left > 0:
                rek(left-1,right,string + "(",T)
            if left < right and right > 0:
                rek(left,right-1, string + ")",T)
                if left > 0 :
                    rek(left-1,right,string+"(", T)
        rek(n,n,string,T)
        return T