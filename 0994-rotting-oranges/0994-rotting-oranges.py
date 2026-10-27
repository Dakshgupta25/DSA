class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m=len(grid),len(grid[0])
        directions=[[1,0],[-1,0],[0,-1],[0,1]]
        queue=deque([])
        res=0
        fresh=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    fresh+=1
        
        while queue and fresh>0:
            for i in range(len(queue)):
                u,v=queue.popleft()
                for x,y in directions:
                    if 0<=u+x<n and 0<=v+y<m and grid[u+x][v+y]==1:
                        queue.append([u+x,v+y])
                        grid[u+x][v+y]=2
                        fresh-=1
            res+=1
        if fresh:
            return -1
        return res

