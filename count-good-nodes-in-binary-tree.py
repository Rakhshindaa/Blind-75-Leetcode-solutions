# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,maxx):
            if not node:
                return 0
            if node.val>=maxx:
                good=1
            else:
                good=0
            maxx=max(maxx,node.val)
            return good + dfs(node.left,maxx)+dfs(node.right,maxx)
        return dfs(root,float('-inf'))
        