# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        history = set()
        cur = head

        while cur is not None:
            if cur in history:
                return True
            history.add(cur)
            cur = cur.next
        return False
