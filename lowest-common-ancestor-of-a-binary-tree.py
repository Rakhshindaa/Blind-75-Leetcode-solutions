# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return
        que = deque([root])
        parent = {root: None}
        
        while que:
            node = que.popleft()
            
            if node.left:
                que.append(node.left)
                parent[node.left] = node
            
            if node.right:
                que.append(node.right)
                parent[node.right] = node
            
            if p in parent and q in parent:
                break
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q:
            if q in ancestors:
                return q
            q = parent[q]
        