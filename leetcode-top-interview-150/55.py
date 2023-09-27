class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lth = len(nums)

        reach = [False] * lth
        reach[0] = True

        for i in range(lth):
            if reach[i]:
                if i + nums[i] + 1 >= lth:
                    return True
                for j in range(i, i + nums[i] + 1):
                    reach[j] = True
            if not reach[i]:
                continue

        return reach[-1]
