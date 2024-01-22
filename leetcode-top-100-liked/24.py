# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prv = dummy

        while (left := prv.next) and (right := prv.next.next):
            prv.next, left.next, right.next = right, right.next, left
            prv = left

        return dummy.next
