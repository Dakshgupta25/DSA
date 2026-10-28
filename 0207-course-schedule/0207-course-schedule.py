class Solution(object):
    def canFinish(self, n, pre):
        indegree= [0]*n
        adj=[[] for _ in range(n)]

        for i,j in pre:
            adj[i].append(j)
        
        for i in range(n):
            for j in adj[i]:
                indegree[j]+=1
        
        queue=deque([])
        completed=0
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                completed+=1
        
        while queue:
            node=queue.popleft()
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    completed+=1
                    queue.append(i)
        
        return completed==n