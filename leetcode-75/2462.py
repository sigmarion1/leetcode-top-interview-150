class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        i = 0
        j = n - 1
        hq1 = []
        hq2 = []

        result = 0

        while k > 0:
            while len(hq1) < candidates and i <= j:
                heappush(hq1, costs[i])
                i += 1

            while len(hq2) < candidates and i <= j:
                heappush(hq2, costs[j])
                j -= 1

            left = hq1[0] if hq1 else float("inf")
            right = hq2[0] if hq2 else float("inf")

            if left <= right:
                result += left
                heappop(hq1)
            else:
                result += right
                heappop(hq2)

            k -= 1

        return result
