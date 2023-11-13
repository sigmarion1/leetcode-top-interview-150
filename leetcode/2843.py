class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            strNum = str(num)
            n = len(strNum)

            if n % 2:
                continue

            l, r, mid = 0, 0, n // 2

            for i in range(n):
                if i < mid:
                    l += int(strNum[i])
                else:
                    r += int(strNum[i])

            if l == r:
                count += 1

        return count
