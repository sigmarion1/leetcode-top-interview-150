# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = None
        cur = None
        rounds = 0

        while l1 or l2:
            if not result:
                result = ListNode()
                cur = result
            else:
                cur.next = ListNode()
                cur = cur.next

            sum_num = rounds
            rounds = 0

            if l1:
                sum_num += l1.val
                l1 = l1.next

            if l2:
                sum_num += l2.val
                l2 = l2.next

            if sum_num >= 10:
                sum_num -= 10
                rounds = 1

            cur.val = sum_num

        if rounds:
            cur.next = ListNode()
            cur = cur.next
            cur.val = rounds

        return result
