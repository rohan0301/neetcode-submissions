class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''

        '''
        result = []
        candidates.sort()
        def backtrack(i, path):
            currSum = sum(path)
            if currSum == target:
                result.append(path)
                return
            if currSum > target or i == len(candidates):
                return
            j = i
            curr = candidates[i]
            while j < len(candidates) and candidates[j] == curr:  
                j += 1
            backtrack(j, path)
            backtrack(i + 1, path + [candidates[i]])
        backtrack(0,[])
        return result