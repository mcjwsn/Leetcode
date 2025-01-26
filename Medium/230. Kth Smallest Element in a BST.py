# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        T = []
        def r(root):
            T.append(root.val)
            if root.left:r(root.left)
            if root.right: r(root.right)
        r(root)
        T.sort()
        return T[k-1]