
class Solution(object):
    def cherryPickup(self, grid):
        n, m = len(grid), len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

        
        def fun(i,j1,j2):
            if j1<0 or j2<0 or j1>=m or j2>=m:
                return -1
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            
            if dp[i][j1][j2] !=-1:
                return dp[i][j1][j2]
            maxi=-1
            for d1 in [-1,0,1]:
                for d2 in [-1,0,1]:
                    val=0
                    if j1==j2:
                        value=grid[i][j1]
                    else:
                        value=grid[i][j1]+grid[i][j2]
                    value+=fun(i+1,j1+d1,j2+d2)
                    maxi=max(maxi,value)
            dp[i][j1][j2]=maxi
            return maxi

        fun(0,0,m-1)
        
        return dp[0][0][m-1]
