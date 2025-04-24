class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        i = 0
        n = len(values)
        while 0 <= i < n:
            if instructions[i] == "jump":
                instructions[i] = ""
                i += values[i]
            elif instructions[i] == "add":
                score += values[i]
                instructions[i] = ""
                i += 1
            else: break
        return score
