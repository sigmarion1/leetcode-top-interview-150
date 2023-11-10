class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        if len(digits) == 1:
            return [1, 0]

        return self.plusOne(digits[:-1]) + [0]
