import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []

        for num in nums:
            heapq.heappush(q, -num)

        kth_max = None

        for _ in range(k):
            kth_max = heapq.heappop(q)

        return -kth_max
