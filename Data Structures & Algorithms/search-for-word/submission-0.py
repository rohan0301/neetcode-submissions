class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        go one by one through teh grid. once starting word is found, dfs until the     word is found. 
        back track when the length of the word is reached and the word is still not found
        store each word by coordinate in the set and whenever we backtrack we remove from the set

        '''
        n = len(board)
        m = len(board[0])
        seen = set()
        def backtrack(row,col,k):
            if k == len(word):
                return True
            if (row < 0 or row >= n or col < 0 or col >= m or (row,col) in seen or board[row][col] != word[k]):
                return False
            seen.add((row,col))
            result = (backtrack(row + 1, col, k + 1) or backtrack(row - 1, col, k+1) or backtrack(row,col + 1, k+1) or backtrack(row, col - 1, k + 1))
            seen.remove((row,col))
            return result
        for i in range(n):
            for j in range(m):
                if backtrack(i,j,0):
                    return True
        return False








