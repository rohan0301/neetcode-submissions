class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        2 pointer through each word. if letters are teh same, increment both
        if they are different, we can 
        1. replace the letter
            both pointers increment and num of changes += 1
        2. add a letter
            word2 gets incremented
        3. delete a letter
            word1 gets incremented
        dfs contains index of word1 and 2
        once one index reaches the end, we can add len(longer word) - len(shorter word) to the count as we have to add that many characters
        '''
        memo = {}
        def dfs(p1, p2):
            if((p1,p2) in memo):
                return memo[(p1,p2)]
            if p1 == len(word1):
                return len(word2) - p2
            if p2 == len(word2):
                return len(word1) - p1
            if word1[p1] == word2[p2]:
                res = dfs(p1 + 1, p2 + 1)
            else:
                res = 1 + min(dfs(p1 + 1, p2 + 1), dfs(p1, p2 + 1), dfs(p1 + 1, p2))
            memo[(p1,p2)] = res
            return res
        return dfs(0,0)
