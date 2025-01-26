class Solution:
    def sortColors(self, nums: List[int]) -> None:
        T = [0,0,0]
        for i in range(len(nums)):
            T[nums[i]]+=1
        j = 0
        for i in range(3):
            while T[i]!=0:
                nums[j] = i
                j+=1
                T[i]-=1
        return nums
        