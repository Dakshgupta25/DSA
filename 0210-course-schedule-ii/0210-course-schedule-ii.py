class Solution(object):
    def findOrder(self, n, pre):
        indegree=[0]*n
        adj=[[] for _ in range(n)]

        for i,j in pre:
            adj[j].append(i)
        
        for i in range(n):
            for j in adj[i]:
                indegree[j]+=1
        
        res=[]
        queue=deque([])
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            node=queue.popleft()
            res.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return [] if len(res)!=n else res
        