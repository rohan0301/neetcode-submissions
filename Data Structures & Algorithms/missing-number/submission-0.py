class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        for i in range(len(nums) + 1):
            sum1 += i
        sum2 = sum(nums)
        if sum1 == sum2:
            return 0
        return sum1 - sum2   
        
