# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeafs(root: Optional[TreeNode]) -> List[TreeNode]:
            result = []
            stack = []

            stack.append(root)

            while stack:
                node = stack.pop()

                if node is None:
                    continue

                if node.left is None and node.right is None:
                    result.append(node.val)

                stack.append(node.right)
                stack.append(node.left)

            return result

        return getLeafs(root1) == getLeafs(root2)
