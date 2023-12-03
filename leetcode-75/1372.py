# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = []
        maxLength = 0

        stack.append(("left", 1, root.left))
        stack.append(("right", 1, root.right))

        while stack:
            direction, length, node = stack.pop()

            if not node:
                continue

            maxLength = max(maxLength, length)

            if direction == "left":
                stack.append(("left", 1, node.left))
                stack.append(("right", length + 1, node.right))
            else:
                stack.append(("right", 1, node.right))
                stack.append(("left", length + 1, node.left))

        return maxLength
