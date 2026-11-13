class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n=len(matrix)
        dp=[[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i==0:
                    dp[i][j]=matrix[i][j]
                elif j==0:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                elif j==n-1:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+matrix[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1])+matrix[i][j]
        return min(dp[n-1])
