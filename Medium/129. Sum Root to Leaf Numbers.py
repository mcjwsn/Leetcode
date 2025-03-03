# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        T = [0]
        def r(root,s):
            if root.left:
                r(root.left, s + str(root.val))
            if root.right: 
                r(root.right, s + str(root.val))
            if not root.left and not root.right:
                print(int(s + str(root.val)))
                T[0] += int(s + str(root.val))
        r(root,"")
        return T[0]