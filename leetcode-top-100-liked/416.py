class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_total = sum(nums)

        if sum_total % 2 == 1:
            return False

        sum_half = int(sum(nums) / 2)

        dp = set([0])

        for num in nums:
            for cur in range(sum_half, num - 1, -1):
                if cur not in dp and cur - num in dp:
                    if cur == sum_half:
                        return True
                    dp.add(cur)

        return False
