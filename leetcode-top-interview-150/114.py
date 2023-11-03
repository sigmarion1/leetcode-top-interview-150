# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        stack = []
        nodes = []
        stack.append(root)

        while stack:
            cur = stack.pop()

            if cur:
                nodes.append(cur)
                stack.append(cur.right)
                stack.append(cur.left)

        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
            nodes[i].left = None
