class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        START, END = 0, 1

        points.sort(key=lambda x: x[0])
        stack = []

        for s, e in points:
            if stack and stack[-1][END] >= s:
                ls, le = stack.pop()
                stack.append([max(s, ls), min(e, le)])
            else:
                stack.append([s, e])

        return len(stack)
