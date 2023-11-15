# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        stack = [(root.left, root.val), (root.right, root.val)]

        while stack:
            node, maxVal = stack.pop()

            if not node:
                continue

            if node.val >= maxVal:
                count += 1
                maxVal = node.val

            stack.append((node.left, maxVal))
            stack.append((node.right, maxVal))

        return count
