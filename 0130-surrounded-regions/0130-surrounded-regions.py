class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        res = [["X"]*m for _ in range(n)]
        visited=[[0]*m for _ in range(n)]

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or visited[i][j]:
                return
            
            if board[i][j]!="O":
                return
            visited[i][j]=1

            res[i][j]="O"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        for i in range(m):
            if board[0][i]=="O":
                dfs(0,i)
            if board[n-1][i]=="O":
                dfs(n-1,i)

        for i in range(n):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][m-1]=="O":
                dfs(i,m-1)

        for i in range(n):
            for j in range(m):
                board[i][j] = res[i][j]