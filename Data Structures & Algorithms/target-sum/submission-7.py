class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        memo = {}
        def backtrack(i, currSum):
            if((i, currSum) in memo):
                return memo[(i, currSum)]
            if i == len(nums):
                if currSum == target:
                    return 1
                return 0
            
            val1 = backtrack(i + 1, currSum + nums[i])
            memo[(i+1,currSum + nums[i])] = val1
            val2 = backtrack(i + 1, currSum - nums[i])
            memo[(i+1, currSum - nums[i])] = val2
            return val1 + val2
            
        return backtrack(0,0)
        