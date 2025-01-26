class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        T = [[nums[0]]]
        for i in range(1, len(nums)):
            flag = False
            for j in range(len(T)):
                if nums[i] not in T[j]:
                    T[j].append(nums[i])
                    flag = True
                    break
            if not flag:T.append([nums[i]])
        return T