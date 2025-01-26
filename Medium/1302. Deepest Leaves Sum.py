# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        deepest = 0
        def find_deepest(root,cnt):
            nonlocal deepest
            if not root.right and not root.left:
                if deepest < cnt:
                    deepest = cnt
                return 0
            if root.left:
                find_deepest(root.left,cnt+1)
            if root.right:
                find_deepest(root.right,cnt+1)
        find_deepest(root,1)
        x = deepest
        def s(root,cnt):
            if not root.right and not root.left:
                if cnt == x:
                    return root.val
                return 0
            if root.left and root.right:
                return s(root.left,cnt+1) + s(root.right,cnt+1)
            elif root.right:
                return s(root.right,cnt+1)
            elif root.left:
                return s(root.left,cnt+1)
        return s(root,1)