class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]

        while len(result) <= n:
            result += [i + 1 for i in result]

        return result[: n + 1]
