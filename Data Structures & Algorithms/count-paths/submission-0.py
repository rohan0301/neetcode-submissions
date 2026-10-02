class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(r, c):
            if ((r,c) in memo):
                return memo[(r,c)]
            if r == m - 1 and c == n - 1:
                return 1
            val1 = 0
            val2 = 0
            if r+1 < m:
                val1 = dfs(r + 1, c)
                memo[(r+1,c)] = val1
            if c+1 < n:
                val2 = dfs(r, c + 1)
                memo[(r, c+1)] = val2
            return val1 + val2
        return dfs(0,0)
            
