# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prv = float("-inf")

        def inorder(node):
            nonlocal prv

            if not node:
                return True

            if not (inorder(node.left) and prv < node.val):
                return False

            prv = node.val

            return inorder(node.right)

        return inorder(root)
