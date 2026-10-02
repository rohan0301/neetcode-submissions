class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        brute force:
            use a hashmap and manually check each row each col and each box
        '''
        row = set()
        col = set()
        square = set()
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] not in row:
                    if board[i][j] != ".":
                        row.add(board[i][j])
                else:
                    print(board[j][i])
                    return False
                if board[j][i] not in col:
                    if board[j][i] != ".":
                        col.add(board[j][i])
                else:
                    print(board[j][i])
                    return False
            row = set()
            col = set()

        #0 + 3 * curr 1 + 3 * curr 2 + 3 * curr
        for i in range(3):
            for l in range(3):
                square = set()
                for j in range(3):
                    for k in range(3):
                        cell = board[3*i + j][3*l + k]
                        if cell not in square:
                            if cell != ".":
                                square.add(cell)
                        else:
                            return False
                       
            
        return True
