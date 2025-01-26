# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        T = [0]
        def r(root):
            if root.right and root.left:
                av,cnt = r(root.right)
                av2,cnt2 = r(root.left)
                if root.val == (av+av2+root.val)//(cnt+cnt2+1):
                    T[0]+=1
                return av+av2+root.val, cnt+cnt2+1
            if root.right:
                av,cnt = r(root.right)
                if root.val == (av+root.val)//(cnt+1):
                    T[0]+=1
                return av+root.val, cnt+1
            if root.left:
                av,cnt = r(root.left)
                if root.val == (root.val+av)//(cnt+1):
                    T[0]+=1
                return av+root.val, cnt+1
            T[0]+=1
            return root.val, 1
        av,cnt = r(root)
        return T[0]