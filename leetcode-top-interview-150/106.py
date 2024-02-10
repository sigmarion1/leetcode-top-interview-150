# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder:
            return None

        curVal = postorder[-1]
        headIndex = inorder.index(curVal)

        cur = TreeNode()

        cur.val = postorder[-1]
        cur.left = self.buildTree(inorder[:headIndex], postorder[:headIndex])
        cur.right = self.buildTree(inorder[headIndex + 1 :], postorder[headIndex:-1])

        return cur
