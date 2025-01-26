# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        T = []
        def r(root):
            T.append(root.val)
            if root.left: r(root.left)
            if root.right:r(root.right)
        if root1: r(root1)
        if root2: r(root2)
        T.sort()
        return T