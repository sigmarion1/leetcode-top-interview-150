class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        numbers = set(nums)

        for num in nums:
            if (num - 1) not in numbers:
                current = num
                count = 1
                while (current + 1) in numbers:
                    current += 1
                    count += 1
                max_count = max(count, max_count)

        return max_count
