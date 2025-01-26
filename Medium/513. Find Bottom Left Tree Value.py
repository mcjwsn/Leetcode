# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = [0]
        def r(root,curr):
            if root.left:
                r(root.left, curr+1)
            if root.right:
                r(root.right,curr+1)
            if root.right == root.left == None:
                d[0] = max(d[0],curr)
            return 0
        rmin = [2**d[0],False]
        def rek(root,dph):
            if root.left:
                rek(root.left,dph+1)
            if root.right:rek(root.right,dph+1)
            if root.right == root.left == None and dph == d[0] and rmin[1]==False:
                rmin[1] = True
                rmin[0] = root.val
            return 0
        r(root,0)
        rek(root,0)
        return rmin[0]