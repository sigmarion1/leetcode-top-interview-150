class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, cur = m - 1, n - 1, m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1

            cur -= 1
