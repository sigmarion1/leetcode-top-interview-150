# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        lvs = []

        q = deque()
        q.append((root, 0))

        while q:
            node, lv = q.popleft()

            if len(lvs) == lv:
                lvs.append([])

            if node.left:
                q.append((node.left, lv + 1))

            if node.right:
                q.append((node.right, lv + 1))

            lvs[lv].append(node.val)

        for i in range(len(lvs)):
            if i % 2:
                lvs[i] = lvs[i][::-1]

        return lvs
