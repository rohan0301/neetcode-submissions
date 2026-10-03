class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = []
        memo = {}
        coins.reverse()
        def backtrack(amountLeft):
            if amountLeft == 0:
                return 0
            if amountLeft in memo:
                return memo[amountLeft]
            highest = float('inf')

            for coin in coins:
                if amountLeft - coin >= 0:
                    highest = min(highest, 1 + backtrack(amountLeft - coin))
            
            memo[amountLeft] = highest
            return highest
        
        minCoins = backtrack(amount)
        return -1 if minCoins == float('inf') else minCoins
            
            