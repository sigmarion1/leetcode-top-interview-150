class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heappush(heap, -num)

        kth_max = None
        for _ in range(k):
            kth_max = heappop(heap)
        return -kth_max
