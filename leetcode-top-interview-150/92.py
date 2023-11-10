# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prv = dummy

        for _ in range(left - 1):
            prv = prv.next

        cur = prv.next

        for _ in range(right - left):
            next_node = cur.next
            cur.next, next_node.next, prv.next = next_node.next, prv.next, next_node

        return dummy.next
