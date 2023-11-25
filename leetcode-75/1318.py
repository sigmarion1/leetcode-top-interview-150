class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0

        while a > 0 or b > 0 or c > 0:
            aBit = a & 1
            bBit = b & 1
            cBit = c & 1

            if cBit:
                if aBit == 0 and bBit == 0:
                    cnt += 1
            else:
                cnt += aBit + bBit

            a >>= 1
            b >>= 1
            c >>= 1

        return cnt
