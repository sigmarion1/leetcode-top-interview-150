class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for a in asteroids:
            while result and result[-1] > 0 and a < 0:
                if result[-1] + a < 0:
                    result.pop()
                elif result[-1] + a > 0:
                    break
                else:
                    result.pop()
                    break
            else:
                result.append(a)

        return result
