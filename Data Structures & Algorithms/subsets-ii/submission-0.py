class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(i, path):
            if i == len(nums):
                result.append(path)
                return
            j = i
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            backtrack(j, path)
            backtrack(i + 1, path + [nums[i]])
        backtrack(0, [])
        return result