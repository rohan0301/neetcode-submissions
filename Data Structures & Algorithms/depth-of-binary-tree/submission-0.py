# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            n = len(queue)
            count += 1
            for i in range(n):
                curr = queue.popleft()
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
        return count -1