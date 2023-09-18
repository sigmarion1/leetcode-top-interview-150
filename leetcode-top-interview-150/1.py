class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            answer = target - nums[i]

            for j in range(len(nums) - 1, i, -1):
                if nums[j] == answer:
                    return [i, j]
