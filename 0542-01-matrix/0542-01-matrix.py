class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n,m=len(mat),len(mat[0])
        dist=[[-1]*m for _ in range(n)]
        queue= deque([])

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    dist[i][j]=0
                    queue.append([i,j])
        
        directions=[(-1,0),(1,0),(0,1),(0,-1)]

        while queue:
            i,j=queue.popleft()
            for u,v in directions:
                ui=u+i
                vj=v+j
                if 0<=ui<n and 0<=vj<m and dist[ui][vj]==-1:
                    dist[ui][vj]=dist[i][j]+1
                    queue.append([ui,vj])
        
        return dist
        