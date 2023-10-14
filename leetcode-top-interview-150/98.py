# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = deque()
        stack.append((root, float("inf"), float("-inf")))

        while stack:
            cur, mx, mi = stack.pop()

            if not mi < cur.val < mx:
                return False

            if cur.left:
                if cur.left.val >= cur.val:
                    return False
                stack.append((cur.left, min(mx, cur.val), mi))
            if cur.right:
                if cur.right.val <= cur.val:
                    return False
                stack.append((cur.right, mx, max(cur.val, mi)))

        return True
