class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        every number in a set
        go through each number:
            if number - 1 not in set start counting sequence
            sequence:
                i = 1
                count = 0
                start = number
                while i < len(nums):
                    if start + i in set:
                        count += 1
                        i += 1
                    else:
                        break
        '''
        if len(nums) == 0:
            return 0
        hashSet = set()
        for num in nums:
            if num not in hashSet:
                hashSet.add(num)
        ##############
        # 2 3
        maxCount = 0
        for num in hashSet:
            if num - 1 not in hashSet:
                i = 1
                count = 1
                while i < len(nums):
                    if num + i in hashSet:
                        count += 1
                        i += 1
                    else:
                        break
                if count > maxCount:
                    maxCount = count
        return maxCount
        