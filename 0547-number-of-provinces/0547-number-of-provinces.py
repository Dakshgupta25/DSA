class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]==1:
                    graph[i].append(j)

        count=0
        visited=[False]*n

        def dfs(node):
            visited[node]=True
            for i in graph[node]:
                if not visited[i]:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count