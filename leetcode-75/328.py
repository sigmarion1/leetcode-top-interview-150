# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyOdd = odd = ListNode()
        dummyEven = even = ListNode()

        cur = head
        isOdd = True

        while cur:
            if isOdd:
                odd.next = cur
                odd = cur
                isOdd = False
            else:
                even.next = cur
                even = cur
                isOdd = True

            cur = cur.next

        even.next = None
        odd.next = dummyEven.next

        return dummyOdd.next
