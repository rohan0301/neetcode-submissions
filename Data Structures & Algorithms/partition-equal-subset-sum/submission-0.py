class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        find half and tehn use dfs to find half the sum
        basecase can be if currsum > halfsum return (backtrack)
        if its equal we have our sum
        
        '''
        targetSum = sum(nums)
        if targetSum % 2 == 1:
            return False
        targetSum = targetSum // 2
        def dfs(i, currSum):
            if currSum == targetSum:
                return True
            if i > len(nums) - 1 or currSum > targetSum:
                return

            if dfs(i + 1, currSum + nums[i]) or dfs(i + 1, currSum):
                return True
            
        result = dfs(0, 0)
        if result is None:
            return False
        return True
            