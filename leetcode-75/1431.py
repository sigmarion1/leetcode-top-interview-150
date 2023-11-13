class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)

        result = [True] * len(candies)

        for i in range(len(result)):
            if candies[i] + extraCandies < maxCandies:
                result[i] = False

        return result
