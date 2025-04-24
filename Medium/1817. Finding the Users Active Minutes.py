class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        s = dict()
        res = [0] * (k)
        for action in logs:
            idx = action[0]
            time = action[1]
            if idx not in s:
                s[idx] = dict()
                s[idx][time] = 1
            else:
                if time not in s[idx]: s[idx][time] = 1
        for dic in s.values(): res[len(list(dic.values()))-1] += 1
        return res