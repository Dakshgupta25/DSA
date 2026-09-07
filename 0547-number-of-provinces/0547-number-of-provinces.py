class Solution(object):
    def findCircleNum(self, isConnected):
        n=len(isConnected)
        visited=[False]*n
        count=0

        def dfs(city):
            for nbr in range(n):
                if isConnected[city][nbr]==1 and visited[nbr]==False:
                    visited[nbr]=True
                    dfs(nbr)
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count