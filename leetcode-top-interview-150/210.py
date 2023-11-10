from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course, require in prerequisites:
            graph[require].append(course)

        in_degree = [0] * numCourses
        for course, require in prerequisites:
            in_degree[course] += 1

        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        result = []

        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) < numCourses:
            return []

        return result
