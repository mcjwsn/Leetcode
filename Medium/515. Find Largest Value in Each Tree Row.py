# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        x = dict()
        def r(root,row):
            if row in x:
                x[row] = max(x[row],root.val)
            else:
                x[row] = root.val
            if root.left:
                r(root.left,row+1)
            if root.right:
                r(root.right,row+1)
        r(root,0)
        return list(x.values())