class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, result):
            result.append(path)

            for i in range(start, len(sn)):
                if i > start and sn[i] == sn[i - 1]:
                    continue
                dfs(i + 1, path + [sn[i]], result)

        sn = sorted(nums)
        result = []
        dfs(0, [], result)

        return result
