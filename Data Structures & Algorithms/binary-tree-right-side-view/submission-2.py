# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        bfs
        start at the root
        for loop 
        '''
        queue = deque()
        queue.append(root)
        result = []
        result2 = []
        while queue:
            n = len(queue)
            #currList = []
            for i in range(n):
                curr = queue.popleft()
                if curr:
                    if i == n-1:
                        result.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            '''
            if currList:
                result.append(currList)
            currList = []

        for lst in result:
            
            result2.append(lst[0])
        '''
        return result
