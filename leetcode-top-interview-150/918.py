class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        curMaxSum = 0
        curMinSum = 0
        maxSum = float("-inf")
        minSum = float("inf")

        for num in nums:
            totalSum += num
            curMaxSum = max(curMaxSum + num, num)
            curMinSum = min(curMinSum + num, num)
            maxSum = max(maxSum, curMaxSum)
            minSum = min(minSum, curMinSum)

        return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)
