class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n - 1
        maxWater = 0

        while l < r:
            currentWater = (r - l) * min(height[l], height[r])
            maxWater = max(maxWater, currentWater)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxWater
