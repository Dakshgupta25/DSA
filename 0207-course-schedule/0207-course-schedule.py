class Solution(object):
    def canFinish(self, n, pre):
        graph=[[] for _ in range(n)]

        for i,j in pre:
            graph[i].append(j)
        
        state=[0]*n

        def dfs(cor):
            if state[cor]==1:
                return False
            if state[cor]==2:
                return True
            state[cor]=1

            for i in graph[cor]:
                if not dfs(i):
                    return False
            state[cor]=2
            return True
        
        for i in range(n):
            if not dfs(i):
                return False
        return True