# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        T = []
        def r(root,depth):
            if len(T) <= depth: T.append([])
            T[depth].append(root.val)
            if root.left: r(root.left,depth+1)
            if root.right: r(root.right,depth+1)
        r(root,0)
        return T      