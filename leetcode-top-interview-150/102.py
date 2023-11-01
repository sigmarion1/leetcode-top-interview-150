# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvs = defaultdict(list)
        q = deque()
        q.append((root, 0))
        lastLv = 0

        while q:
            cur, lv = q.popleft()

            if not cur:
                continue

            lvs[lv].append(cur.val)

            if cur.left:
                q.append((cur.left, lv + 1))
            if cur.right:
                q.append((cur.right, lv + 1))

        return [lvs[i] for i in range(len(lvs))]
