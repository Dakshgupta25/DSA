class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        # Build graph
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely processed
        state = [0] * numCourses

        def dfs(course):

            # Cycle found
            if state[course] == 1:
                return False

            # Already checked this course
            if state[course] == 2:
                return True

            # Currently exploring
            state[course] = 1

            for prerequisite in graph[course]:

                if not dfs(prerequisite):
                    return False

            # Finished exploring this course
            state[course] = 2

            return True

        for course in range(numCourses):

            if not dfs(course):
                return False

        return True