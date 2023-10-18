class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lth = len(nums)

        result = [-1, -1]

        if lth < 4:
            found = False
            for i in range(lth):
                if nums[i] == target and not found:
                    result = [i, i]
                    found = True
                elif nums[i] == target and found:
                    result[1] = i
                else:
                    found = False

            return result

        mid = lth // 2

        if nums[mid] < target:
            right = self.searchRange(nums[mid:], target)
            result = [x if x == -1 else x + mid for x in right]
        elif nums[mid] > target:
            result = self.searchRange(nums[:mid], target)
        else:
            left = self.searchRange(nums[: mid + 1], target)
            right = self.searchRange(nums[mid:], target)
            result = [left[0], right[1] + mid]
        return result
