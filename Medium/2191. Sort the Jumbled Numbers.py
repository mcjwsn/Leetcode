class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def nwm(x):
            T = []
            if x == 0: return mapping[x]
            while x > 0:
                T.append(x%10)
                x//=10
            for i in range(len(T)):
                T[i] = mapping[T[i]]
            s = 0
            p = 0
            while T:
                s+=T[0]*(10**p)
                p+=1
                T = T[1:]
            return s
        for i in range(len(nums)):
            nums[i] = [nums[i],nwm(nums[i])]
        nums = sorted(nums, key = lambda x:x[1])
        for i in range(len(nums)):
            nums[i] = nums[i][0]
        return nums