/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun getIntersectionNode(headA:ListNode?, headB:ListNode?):ListNode? {
        
        var curA = headA
        var curB = headB

        var m = 0
        var n = 0

        while(curA != null || curB != null) {
            if(curA != null) {
                m += 1
                curA = curA.next
            }

            if(curB != null) {
                n += 1
                curB = curB.next
            }
        }

        curA = headA
        curB = headB

        while(m != n) {
            if(m > n) {
                curA = curA!!.next
                m -= 1
            } else if(m < n) {
                curB = curB!!.next
                n -= 1
            }
        }

        while(curA != null || curB != null) {
            if(curA == curB) {
                return curA
            }

            curA = curA?.next
            curB = curB?.next
        }

        return null

    }
}