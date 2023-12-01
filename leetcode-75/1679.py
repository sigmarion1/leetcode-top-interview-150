class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        count = 0

        nums.sort()

        while left < right:
            curSum = nums[left] + nums[right]
            if curSum == k:
                count += 1
                left += 1
                right -= 1
            elif curSum < k:
                left += 1
            else:
                right -= 1

        return count
