class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        values = [i for i in range(1, n + 1)]
        res = []

        def rec(current, nVals, count):
            if not count:
                res.append(current)
                return

            if not nVals:
                return

            for i in range(len(nVals)):
                rec(current + [nVals[i]], nVals[i + 1 :], count - 1)

        rec([], values, k)

        return res
