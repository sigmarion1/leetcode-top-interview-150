class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            return l

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]
