# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        vals = []

        while stack:
            cur = stack.pop()
            vals.append(cur.val)

            if cur.left is not None:
                stack.append(cur.left)

            if cur.right is not None:
                stack.append(cur.right)

        vals.sort()

        return vals[k - 1]
