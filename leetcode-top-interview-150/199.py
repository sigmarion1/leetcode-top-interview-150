# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        result = []
        q.append(root)

        while q:
            cq = deque()
            prv = -1
            while q:
                cur = q.popleft()

                if cur.left is not None:
                    cq.append(cur.left)

                if cur.right is not None:
                    cq.append(cur.right)

                prv = cur

            result.append(prv.val)
            q = cq

        return result
