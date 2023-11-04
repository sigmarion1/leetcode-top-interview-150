class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preCourses = defaultdict(list)

        for course, preCourse in prerequisites:
            preCourses[course].append(preCourse)

        def canFinishCourse(course, history):
            if course in history:
                return False
            if course not in preCourses:
                return True

            history.add(course)

            for preCourse in preCourses[course]:
                if not canFinishCourse(preCourse, history):
                    return False

            history.remove(course)

            del preCourses[course]
            return True

        for course in range(numCourses):
            if not canFinishCourse(course, set()):
                return False

        return True
