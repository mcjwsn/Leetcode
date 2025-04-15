class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if not digits: return []
        if len(digits) == 1: return list(d[digits[0]])
        for v in d: d[v] = list(d[v])
        T = []
        def r(curr):
            nonlocal digits
            if len(digits) == len(curr):
                T.append(curr)
                return
            for v in d[digits[len(curr)]]:
                r(curr + v)
        for v in d[digits[0]]: r(v)
        return T