"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        q = deque()
        q.append((root, 0))
        prv, prvLv = None, None

        while q:
            cur, curLv = q.popleft()

            if not cur:
                continue

            if prv and prvLv == curLv:
                prv.next = cur

            if cur.left:
                q.append((cur.left, curLv + 1))
            if cur.right:
                q.append((cur.right, curLv + 1))

            prv, prvLv = cur, curLv

        return root
