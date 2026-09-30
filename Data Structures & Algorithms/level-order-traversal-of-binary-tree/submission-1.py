# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            n = len(queue)
            currList = []
            for i in range(n): 
                curr = queue.popleft()
                if curr:
                    currList.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if currList:        
                result.append(currList)
        return result