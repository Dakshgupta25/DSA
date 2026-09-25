class Solution(object):
    def findOrder(self, n, pre):
        graph=[[] for _ in range(n)]

        for i,j in pre:
            graph[i].append(j)
        
        state=[0]*n
        res=[]
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
            res.append(cor)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        return res