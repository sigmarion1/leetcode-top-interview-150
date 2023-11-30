# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        maxLv = 0
        q = deque()
        q.append((1, [root]))

        while q:
            lv, nodes = q.popleft()

            childNodes = []
            curSum = 0

            for node in nodes:
                curSum += node.val

                if node.right:
                    childNodes.append(node.right)
                if node.left:
                    childNodes.append(node.left)

            if curSum > maxSum:
                maxSum = curSum
                maxLv = lv

            if childNodes:
                q.append((lv + 1, childNodes))

        return maxLv
