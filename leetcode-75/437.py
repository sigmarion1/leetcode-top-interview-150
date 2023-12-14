# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0

        def rec(sums, node):
            if not node:
                return

            nonlocal count

            nextSum = sums[:]
            nextSum.append(0)

            for i in range(len(nextSum)):
                nextSum[i] += node.val
                if nextSum[i] == targetSum:
                    count += 1

            rec(nextSum, node.left)
            rec(nextSum, node.right)

        rec([], root)

        return count
