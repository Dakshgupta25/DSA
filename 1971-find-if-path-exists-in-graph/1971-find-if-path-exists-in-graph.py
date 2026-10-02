class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph=[[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[0]*n
        def dfs(node):
            if visited[node]==1:
                return False
            visited[node]=1
            if node==destination:
                return True
            for i in graph[node]:
                if dfs(i):
                    return True
            return False
        return dfs(source)
