class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def recur(arr, remain):
            result.append(arr)

            for i in range(len(remain)):
                cur = arr[:] + [remain[i]]
                next_remain = remain[i + 1 :]
                recur(cur, next_remain)

        recur([], nums)

        return result
