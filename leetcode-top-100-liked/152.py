class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]

        maxVal = nums[0]
        minVal = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == 0:
                maxVal = 0
                minVal = 0
            else:
                val1 = maxVal * nums[i]
                val2 = minVal * nums[i]
                maxVal = max(val1, val2, nums[i])
                minVal = min(val1, val2, nums[i])

            result = max(result, maxVal)

        return result
