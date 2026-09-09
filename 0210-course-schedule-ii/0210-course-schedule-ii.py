class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph=[[] for _ in range(numCourses)]

        state=[0]*numCourses
        res=[]
        for u,v in prerequisites:
            graph[u].append(v)

        def dfs(node):
            if state[node]==1:
                return False
            if state[node]==2:
                return True
            state[node]=1
            for nbr in graph[node]:
                if not dfs(nbr):
                    return False
            state[node]=2
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        