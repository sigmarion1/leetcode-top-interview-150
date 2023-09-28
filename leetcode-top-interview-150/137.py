class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lth = len(nums)

        if lth == 1:
            return nums[0]

        nums.sort()

        cur = None

        if nums[0] != nums[1]:
            return nums[0]

        for i in range(1, lth - 2):
            if (nums[i] != nums[i + 1]) and (nums[i + 1] != nums[i + 2]):
                return nums[i + 1]

        return nums[-1]
