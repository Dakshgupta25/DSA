class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        n=len(image)
        m=len(image[0])
        og=image[sr][sc]
        visited=[[0]*m for _ in range(n)]
        direction=[[-1,0],[1,0],[0,-1],[0,1]]
        def bfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or visited[i][j]:
                return 
            visited[i][j]=1
            if image[i][j]!=og:
                return
            image[i][j]=color
            for x,y in direction:
                bfs(i+x,j+y)
            return 
        bfs(sr,sc)
        return image
            