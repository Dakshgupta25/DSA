class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list: [course, prereq] -> prereq points to course
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[prereq].append(course)

        # 0 = unvisited, 1 = visiting (in current recursion stack), 2 = visited
        state = [0] * numCourses
        st = []

        def go(u):
            state[u] = 1  # Mark as visiting

            for v in adj[u]:
                if state[v] == 1:
                    return False  # Cycle detected!
                if state[v] == 0:
                    if not go(v):
                        return False

            state[u] = 2  # Mark as completely visited
            st.append(u)
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not go(i):
                    return []  # Return empty list if impossible due to cycle

        return st[::-1]