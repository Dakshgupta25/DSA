class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        dp = [[1]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

        # Handle first row
        for j in range(1, n):
            if dp[0][j-1] == 0:
                dp[0][j] = 0

        # Handle first column
        for i in range(1, m):
            if dp[i-1][0] == 0:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] != 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]