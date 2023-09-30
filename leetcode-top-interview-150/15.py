class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lth = len(nums)
        asr = []

        nums.sort()

        for i in range(lth - 2):
            nums[i]
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = lth - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triple = [nums[i], nums[l], nums[r]]
                    asr.append(triple)
                    while l < r and nums[l] == triple[1]:
                        l += 1
                    while l < r and nums[r] == triple[2]:
                        r -= 1

        return asr
