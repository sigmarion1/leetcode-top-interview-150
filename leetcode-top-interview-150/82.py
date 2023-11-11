# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(-200, head)

        prv = dummy
        cur = head
        duVal = -200

        while cur:
            if duVal == cur.val:
                prv.next, cur = cur.next, cur.next
            elif cur.next and cur.val == cur.next.val:
                duVal = cur.val
                prv.next, cur = cur.next, cur.next
            else:
                prv, cur = cur, cur.next

        return dummy.next
