class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1

        sorted_dict = sorted(num_dict.items(), reverse=True, key=lambda x: x[1])

        return [sorted_dict[i][0] for i in range(k)]
