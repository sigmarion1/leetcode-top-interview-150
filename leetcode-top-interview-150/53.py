class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -float("inf")
        curSum = 0

        for num in nums:
            curSum += num

            maxSum = max(curSum, maxSum)
            curSum = 0 if curSum < 0 else curSum

        return maxSum
