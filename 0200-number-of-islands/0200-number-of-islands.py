class Solution(object):
    def numIslands(self, grid):
        
        n,m=len(grid),len(grid[0])
        visited=[[0]*m for _ in range(n)]

        res=0
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or visited[i][j] or grid[i][j]=="0":
                return 
            visited[i][j]=1
            for x,y in directions:
                dfs(i+x,j+y)
            return
        for x in range(n):
            for y in range(m):
                if not visited[x][y] and grid[x][y]=="1":
                    dfs(x,y)
                    res+=1
        return res
            
            

            