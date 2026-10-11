class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        find half and tehn use dfs to find half the sum
        basecase can be if currsum > halfsum return (backtrack)
        if its equal we have our sum
        
        '''
        memo = {}
        targetSum = sum(nums)
        if targetSum % 2 == 1:
            return False
        targetSum = targetSum // 2
        def dfs(i, currSum):
            if((i, currSum) in memo):
                return memo[(i, currSum)]
            if currSum == targetSum:
                return True
            if i > len(nums) - 1 or currSum > targetSum:
                return
            result1 = dfs(i+1, currSum + nums[i])
            if((i+1, currSum + nums[i]) not in memo):
                memo[(i+1, currSum + nums[i])] = result1
            result2 = dfs(i+1, currSum)
            if ((i+1, currSum) not in memo):
                memo[(i+1, currSum)] = result2
            if result1 or result2:
                return True
            
        result = dfs(0, 0)
        if result is None:
            return False
        return True
            