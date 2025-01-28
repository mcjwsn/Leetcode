# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        T = [root.val]
        def r(root):
            if not root.left and not root.right: return root.val
            elif root.left and not root.right:
                root.val = max(root.val,root.val+r(root.left))
                return root.val
            elif root.right and not root.left:
                root.val = max(root.val + r(root.right),root.val)
                return root.val
            else:
                root.val = max(max(r(root.left),r(root.right)) + root.val, root.val)
                return root.val
        r(root)
        def r2(root):
            if not root.left and not root.right:
                #print(root.val)
                T[0] = max(T[0], root.val)
            elif not root.left and root.right:
               # print(root.val)
                T[0] = max(T[0],root.val)
                r2(root.right)
            elif not root.right and root.left:
                #print(root.val)
                T[0] = max(T[0],root.val)
                r2(root.left)
            else:
                #print(root.val)
                T[0] = max(T[0],min(root.left.val,root.right.val)+root.val,root.val)
                r2(root.left)
                r2(root.right)
        r2(root)
        return T[0]
