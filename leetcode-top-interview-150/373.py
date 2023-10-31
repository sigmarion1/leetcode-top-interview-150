class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        result = []

        from heapq import heappush, heappop

        m, n, visited = len(nums1), len(nums2), set()

        if m == 0 or n == 0:
            return []

        q = [(nums1[0] + nums2[0], (0, 0))]

        for _ in range(min(k, m * n)):
            val, (i, j) = heappop(q)
            result.append([nums1[i], nums2[j]])

            if i + 1 < m and (i + 1, j) not in visited:
                heappush(q, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visited:
                heappush(q, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))

        return result
