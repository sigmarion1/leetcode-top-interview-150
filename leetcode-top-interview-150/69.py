class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 1, x

        while l < r:
            mid = (l + r) // 2
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid

        if l * l > x:
            return l - 1
        else:
            return l
