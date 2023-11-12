class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        lH, rH = [0] * n, [0] * n
        lMax, rMax = 0, 0

        for i in range(n):
            lMax = max(lMax, height[i])
            lH[i] = lMax

        for i in range(n - 1, -1, -1):
            rMax = max(rMax, height[i])
            rH[i] = rMax

        water = [min(lH[i], rH[i]) - height[i] for i in range(n)]

        return sum(water)
