class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []

        for num in nums:
            if num != val:
                result.append(num)

        nums[:] = result

        return len(nums)
