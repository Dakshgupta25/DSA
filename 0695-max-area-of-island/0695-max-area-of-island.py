class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])

        visited=[[0]*m for _ in range(n)]
        
        def dfs(i,j):
            if n<=i or i<0 or m<=j or j<0 or visited[i][j] or grid[i][j]==0:
                return 0

            visited[i][j]=1
            return(1+dfs(i-1,j)+dfs(i,j-1)+dfs(i+1,j)+dfs(i,j+1))
            
        res=0
        for i in range(n):
            for j in range(m):
                if visited[i][j]==0 and grid[i][j]==1:
                    res=max(res,dfs(i,j))
        return res
