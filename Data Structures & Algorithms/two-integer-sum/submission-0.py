class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            contrast = target - nums[i]
            if contrast in hm:
                return [hm[contrast], i]
            hm[nums[i]] = i
        return 0