class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            if n < 0:
                return 0
            val1 = dfs(n-1)
            memo[n-1] = val1
            val2 = dfs(n-2)
            memo[n-2] = val2
            return val1 + val2
        return dfs(n)