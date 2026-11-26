class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)

        dp=[[-1]*m for i in range(n)]

        def solve(i,j):
            if i==n:
                return m-j
            elif j==m:
                return n-i
            if dp[i][j]!=-1:
                return dp[i][j]
            
            if word1[i]==word2[j]:
                dp[i][j]= solve(i+1,j+1)
                return dp[i][j]
            else:
                dp[i][j]=1+min(solve(i+1,j),solve(i,j+1))
                return dp[i][j]
        return solve(0,0)