class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        backtracking
        we can either stick to the same coin, go to the next. ends when number is greater than amount or i == len(coins)
        '''
        hm = {}
        def backtrack(i, currSum):
            if ((i,currSum) in hm):
                return hm[(i,currSum)]
            if currSum == amount:
                return 1
            if i == len(coins) or currSum > amount:
                return 0
            
            val1 = backtrack(i, currSum + coins[i])
            if ((i,currSum+ coins[i]) not in hm):
                hm[(i,currSum + coins[i])] = val1
            val2 = backtrack(i + 1, currSum)
            if ((i + 1,currSum) not in hm):
                hm[(i+1,currSum)] = val2
            else:
                val1 = hm[(i, currSum + coins[i])]
                val2 = hm[(i+1,currSum)]
            return val1 + val2
        val = backtrack(0,0)
        return val
            
    