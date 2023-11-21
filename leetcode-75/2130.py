# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        count = 0

        cur = head

        while cur:
            stack.append(cur)
            count += 1

            cur = cur.next

        count //= 2

        maxSum = float("-inf")

        cur = head

        while count:
            leftVal = cur.val
            rightVal = stack.pop().val

            maxSum = max(maxSum, leftVal + rightVal)
            cur = cur.next
            count -= 1

        return maxSum
