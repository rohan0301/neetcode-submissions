class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        decision tree and at each decision we have the same number or we have the next  number in the path or we can skip it
        '''
        result = []
        def backtrack(i,path): # '''currSum,''' 
            currSum = sum(path) if path else 0
            if currSum == target:
                result.append(path)
                return
            if currSum > target or i == len(nums):
                return
            backtrack(i, path + [nums[i]])#'''sum((path + [nums[i]])),'''
            backtrack(i + 1,path)#'''sum(path),''' 

        backtrack(0,[])
        return result