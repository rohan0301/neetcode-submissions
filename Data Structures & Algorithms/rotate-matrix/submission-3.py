class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''
        4 pointers for each corner tl tr bl br
        top bottom left right
        once it reaches the other side move to original spot then inside   by k where k starts at 0 and goes until it *passes* n//2 
        each index for each pointer is + or - k depending on what it is
        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        '''
        n = len(matrix)
        k = 0
        top, bottom, left, right = 0, n - 1, 0, n - 1
        while k <= n//2:
            top, bottom, left, right = 0 + k, n - 1 - k, 0 + k, n - 1 - k
            print(f"top: {top}, bottom: {bottom}, left: {left}, right: {right}")
            for i in range(n - (k*2) - 1):
                print(f"i is {i}")
                #top -> right
                temp = matrix[top+i][right]
                matrix[top + i][right] = matrix[top][left + i]

                print(f"{matrix[top][left+i]} -> {matrix[top + i][right]}")
                #right -> bottom
                temp2 = matrix[bottom][right - i]
                matrix[bottom][right - i] = temp
                print(f"{temp} -> {matrix[bottom][right - i]}")
                #matrix[top + i][right], matrix[bottom][right - i] = matrix[bottom][right - i], matrix[top - i][right]

                #bottom -> left
                temp = matrix[bottom - i][left]
                matrix[bottom - i][left] = temp2
                print(f"{temp2} -> {matrix[bottom - i][left]}")
                #matrix[bottom][right - i], matrix[bottom - i][left] = matrix[bottom - i][left], matrix[bottom][right - i]

                #left -> top
                matrix[top][left + i] = temp
                print(f"{temp} -> {matrix[top][left + i]}")
                #matrix[bottom - i][left], matrix[top][left + i] = matrix[top][left + i], matrix[bottom - i][left]
            k += 1
            
         
        