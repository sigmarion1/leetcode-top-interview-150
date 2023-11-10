# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        lhead, rhead = ListNode(), ListNode()
        l, r = lhead, rhead

        cur = head

        while cur:
            if cur.val < x:
                l.next = cur
                l = cur
            else:
                r.next = cur
                r = cur

            cur = cur.next

        r.next = None
        l.next = rhead.next

        return lhead.next
