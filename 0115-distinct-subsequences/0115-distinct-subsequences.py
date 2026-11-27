class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        n=len(s)
        m=len(t)

        dp=[[-1]*m for i in range(n)]

        def solve(i,j):
            if j==m:
                return 1
            if i==n :
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]=solve(i+1,j+1)+solve(i+1,j)
            else:
                dp[i][j]=solve(i+1,j)
            return dp[i][j]
        return solve(0,0)
