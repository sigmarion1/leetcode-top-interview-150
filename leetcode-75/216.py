class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def rec(cur, target):
            if target == 0 and len(cur) == k:
                result.append(cur)

            if len(cur) >= k:
                return

            if cur and target <= cur[-1]:
                return

            start = cur[-1] + 1 if cur else 1

            for i in range(start, 10):
                rec(cur + [i], target - i)

        rec([], n)

        return result
