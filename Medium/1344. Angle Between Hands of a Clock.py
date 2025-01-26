class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour += minutes/60
        minutes/=5
        l = min(abs(hour-minutes),abs(minutes-hour))
        res = l*30
        return min(360-res,res)