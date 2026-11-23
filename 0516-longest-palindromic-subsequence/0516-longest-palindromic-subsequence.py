class Solution(object):
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = {}
        def solve(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            if (l, r) in dp:
                return dp[(l, r)]
            if s[l] == s[r]:
                dp[(l, r)] = 2 + solve(l + 1, r - 1)
            else:
                dp[(l, r)] = max(
                    solve(l + 1, r),
                    solve(l, r - 1)
                )
            return dp[(l, r)]
        return solve(0, n - 1)
