class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        n = len(milestones)
        if n==1: return 1
        x = max(milestones)
        s = sum(milestones)-x
        if s-x<0: return 2*s+1
        return s+x
        