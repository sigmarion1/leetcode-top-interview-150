class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def rec(pals, remain):
            if len(remain) == 0:
                result.append(pals)
                return

            cur = []

            for i in range(len(remain)):
                cur.append(remain[i])

                if cur == cur[::-1]:
                    rec(pals + ["".join(cur)], remain[i + 1 :])

            return

        rec([], s)

        return result
