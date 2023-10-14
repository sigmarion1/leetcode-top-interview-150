# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        numbers = []
        stack = deque()
        stack.append((root, ""))

        while stack:
            cur, number = stack.pop()
            new_number = number + str(cur.val)

            if cur.left is None and cur.right is None:
                numbers.append(new_number)
                continue

            if cur.left is not None:
                stack.append((cur.left, new_number))
            if cur.right is not None:
                stack.append((cur.right, new_number))

        val = 0

        for number in numbers:
            val += int(number)

        return val
