# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        values = defaultdict(list)
        q = deque()

        q.append((root, 1))

        while q:
            cur, lv = q.popleft()
            values[lv].append(cur.val)

            if cur.left:
                q.append((cur.left, lv + 1))
            if cur.right:
                q.append((cur.right, lv + 1))

        result = []
        i = 1

        while i in values:
            result.append(sum(values[i]) / len(values[i]))
            i += 1

        return result
