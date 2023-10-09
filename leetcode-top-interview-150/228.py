class Solution:
    def toStr(self, start, end):
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        result = []
        start = None
        prv = None

        for num in nums:
            if start is None:
                start = num
                prv = num
            elif start is not None:
                if num > prv + 1:
                    result.append(self.toStr(start, prv))
                    start = num
                    prv = num
                else:
                    prv = num

        result.append(self.toStr(start, nums[-1]))

        return result
