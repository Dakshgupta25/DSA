class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        dp=[[-1]*n for i in range(n)]
        def solve(l,r):
            if l>=r:
                return 0
            if dp[l][r]!=-1:
                return dp[l][r]

            if s[l]==s[r]:
                dp[l][r]=solve(l+1,r-1)
                return dp[l][r]
            else:
                dp[l][r]= 1+ min(solve(l+1,r),solve(l,r-1))
                return dp[l][r]
        return solve(0,n-1)

