class Solution:
    def findMin(self, nums: List[int]) -> int:
        lth = len(nums)
        half = int(lth / 2)

        if lth <= 4:
            return min(nums)

        a, b, c, d = nums[0], nums[half - 1], nums[half], nums[-1]
        min_nums = min(a, b, c, d)

        if min_nums in (a, b):
            return self.findMin(nums[0:half])

        else:
            return self.findMin(nums[half:])
