class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        graph= [[] for _ in range(n)]
        visited=[False]*n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node):
            if node==destination:
                return True
            visited[node]=True
            for nbr in graph[node]:
                if not visited[nbr]:
                    if dfs(nbr):
                        return True
            return False
        return dfs(source)