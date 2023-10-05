# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        lth = 0
        cur = head
        prv = None

        while cur is not None:
            lth += 1
            prv = cur
            cur = cur.next

        prvTail = prv

        modK = k % lth

        if lth == 1 or modK == 0:
            return head

        newTailN = lth - modK - 1
        cur = head

        while newTailN > 0:
            newTailN -= 1
            cur = cur.next

        newTail = cur
        newHead = cur.next

        newTail.next = None
        prvTail.next = head

        return newHead
