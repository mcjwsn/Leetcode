class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        a = len(customers)
        res = customers[0][1]
        start_time = customers[0][1]+customers[0][0]
        for i in range(1,a):
            start_time = max(start_time, customers[i][0])
            res += start_time + customers[i][1] - customers[i][0]
            start_time += customers[i][1]
        return res/a