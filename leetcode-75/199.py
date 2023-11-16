# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightDict = OrderedDict()
        q = deque()
        q.append((root, 0))

        while q:
            node, lv = q.popleft()

            if not node:
                continue

            rightDict[lv] = node.val

            q.append((node.left, lv + 1))
            q.append((node.right, lv + 1))

        return [x for x in rightDict.values()]
