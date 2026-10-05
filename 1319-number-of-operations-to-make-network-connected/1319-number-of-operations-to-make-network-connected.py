class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections)<n-1:
            return -1
        graph=[[] for _ in range(n)]
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        part=0
        def dfs(node):
            visited[node]=True
            for i in graph[node]:
                if not visited[i]:
                    dfs(i)
        for i in range(n):
            if not visited[i]:
                part+=1
                dfs(i)
        return part-1
