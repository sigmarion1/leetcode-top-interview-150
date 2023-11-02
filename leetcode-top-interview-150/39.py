class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        numbers = sorted(candidates)

        def recurSum(cur, numbers):
            if sum(cur) == target:
                results.append(cur)
            elif sum(cur) > target:
                return

            for i in range(len(numbers)):
                recurSum(cur + [numbers[i]], numbers[i:])

        recurSum([], numbers)

        return results
