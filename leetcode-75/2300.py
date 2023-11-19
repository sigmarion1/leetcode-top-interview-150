class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        n = len(spells)
        m = len(potions)
        ans = [0] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            potion_need = (success + spell - 1) // spell
            left, right = 0, m

            while left < right:
                mid = (left + right) // 2

                if potions[mid] >= potion_need:
                    right = mid
                else:
                    left = mid + 1

            ans[i] = m - left

        return ans
