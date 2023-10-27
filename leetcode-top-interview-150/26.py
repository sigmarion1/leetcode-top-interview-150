class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lth = len(nums)

        current = nums[0]
        count = 1

        for i in range(1, lth):
            if current != nums[i]:
                current = nums[i]
                nums[count] = current
                count = count + 1
        return count
