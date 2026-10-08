# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        hm = {}
        def dfs(node, highest):
            if not node:
                return
            if node.val >= highest:
                highest = node.val
            hm[node] = highest 

            dfs(node.left, hm[node])
            dfs(node.right, hm[node])
        dfs(root, root.val)
        for key in hm:
            if hm[key] == key.val:
                count += 1
        return count