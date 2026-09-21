class Solution(object):
    def numIslands(self, grid):
        
        n=len(grid)
        m=len(grid[0])

        visited=[[0]*m for _ in range(n) ]
        cnt=0

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or visited[i][j] or grid[i][j]=="0":
                return
            visited[i][j]=1

            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]=="1":
                    cnt+=1
                    dfs(i,j)
        return cnt

            