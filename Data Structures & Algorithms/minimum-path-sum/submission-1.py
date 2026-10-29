from collections import defaultdict
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        start 0 0
        dfs every path
        till end 
        '''
        endr = len(grid) - 1
        endc = len(grid[0]) - 1
        d = [(1,0), (0,1)]
        memo = defaultdict(list)
        def dfs(r,c, currSum):
            #currSum += grid[r][c]
            result = float('inf')
            if r == endr and c == endc:
                return grid[r][c]
            if (r,c) in memo:
                return memo[(r,c)]
            for radd, cadd in d:
                nrow = r + radd
                ncol = c + cadd
                if nrow <= endr and ncol <= endc:
                    result = min(result, dfs(nrow,ncol, currSum))
            memo[(r,c)] = result + grid[r][c]
            return memo[(r,c)]
        return dfs(0,0,0)
        

        