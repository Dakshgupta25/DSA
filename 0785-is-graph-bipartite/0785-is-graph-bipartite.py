class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n=len(graph)
        color=[-1]*n
        
        for start in range(n):
            if color[start]!=-1:
                continue
            queue=deque([start])
            color[start]=True
            
            while queue:
                for i in range(len(queue)):
                    node=queue.popleft()
                    for j in graph[node]:
                        if color[j]==-1:
                            color[j]= not color[node]
                            queue.append(j)
                        elif color[j]==color[node]:
                            return False
            
        return True
                        